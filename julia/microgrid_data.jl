using Convex
using SCS
using PyPlot

PLOT_FIGURES = true # True to plot figures, false to suppress plots
N = 96 # Number of periods in the day (so each interval 15 minutes)

# Convenience variables for plotting
fig_size = [14,3];
xtick_vals = [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96];
xtick_labels = ["0:00", "2:00am", "4:00am", "5:00am", "8:00am", "10:00am", "12:00pm", "2:00pm", "4:00pm", "6:00pm", "8:00pm", "10:00pm", "12:00am"];


#############################################
# Price data generation - price values and intervals based off of PG&E Time Of Use plans
#############################################
partial_peak_start = 34   # 08:30
peak_start = 48           # 12:00
peak_end = 72             # 18:00 (6:00pm)
partial_peak_end = 86     # 21:30 (9:30pm)

off_peak_inds = vcat(1:partial_peak_start, partial_peak_end+1:N);
partial_peak_inds = vcat(partial_peak_start+1:peak_start, peak_end+1:partial_peak_end);
peak_inds = vcat(peak_start+1:peak_end);

# rates in $ / kWh
off_peak_buy = 0.14;
partial_peak_buy = 0.25;
peak_buy = 0.45;

# Rate cuts from buy prices to get sell prices
off_peak_perc_cut = 0.20;
partial_peak_perc_cut = 0.12;
peak_perc_cut = 0.11;

off_peak_sell = (1 - off_peak_perc_cut) * off_peak_buy;
partial_peak_sell = (1 - partial_peak_perc_cut) * partial_peak_buy;
peak_sell = (1 - peak_perc_cut) * peak_buy;

# Combine the buy and sell prices into the price vectors
R_buy = zeros(N);
R_buy[off_peak_inds] .= off_peak_buy;
R_buy[partial_peak_inds] .= partial_peak_buy;
R_buy[peak_inds] .= peak_buy;

R_sell = zeros(N);
R_sell[off_peak_inds] .= off_peak_sell;
R_sell[partial_peak_inds] .= partial_peak_sell;
R_sell[peak_inds] .= peak_sell;

# Plot the prices
if PLOT_FIGURES
    figure(figsize=fig_size);
    plot(R_buy, label="Buy Price");
    plot(R_sell, label="Sell Price");
    legend();
    ylabel("Price (\$ / kWh)");
    title("Energy Prices (\$ / kWh)", fontsize=19);
    xticks(xtick_vals, xtick_labels );
end;

#############################################
# Solar data generation
#############################################
# Just something simple: a shifted cosine wave, squared to smooth edges, peak at noon
# Some random +1 and +2 here and there to make it match python code exactly
shift = (N/2);
my_vec = ((1:N) .- shift .- 1) .* 2 .* pi ./ N
p_pv = cos.(my_vec).^2;

scale_factor = 35
p_pv = p_pv * scale_factor
p_pv = max.(p_pv,0)
p_pv[1:Int(shift/2)+1] .= 0
p_pv[N-Int(shift/2)+2:N] .= 0

# Plot it
if PLOT_FIGURES
    figure(figsize=fig_size)
    plot(p_pv)
    title("PV Curve (kW)", fontsize=19)
    ylabel("Power (kW)")
    xticks(xtick_vals, xtick_labels )
end;

#############################################
# Load Data Generation (using cvx)
#############################################
# Fit a curve to some handpicked points and constrain the end points
# to match and the derivative at the end to be the same at the beginning

# points to fit to
points = [
    [1, 7],
    [11, 8],
    [21, 10],
    [29, 15],
    [37, 21],
    [46, 23],
    [53, 21],
    [57, 18],
    [61, 22.5],
    [67, 24.3],
    [71, 25],
    [74, 24],
    [84, 19],
    [96, 7],
]

# Formulate an optimization problem that minimizes the error of 
# the fit while also minimizing the 2nd order difference of the function
p_ld = Variable(N)
obj_val = Variable(N + length(points))

prob = minimize(sum(obj_val))

# constr = []

prob.constraints += p_ld[1] == p_ld[N];
prob.constraints += (p_ld[2] - p_ld[1]) == (p_ld[N] - p_ld[N-1]);

# Add a squared fitting error to the objective
for i=1:length(points)
    prob.constraints += obj_val[i] >= square(p_ld[points[i][1]] - points[i][2]);
end

# Add the second order difference to the objective
for i=2:N-1
    prob.constraints += obj_val[i+length(points)] >= 100*square(p_ld[i+1] - 2*p_ld[i] + p_ld[i-1]);
end

prob.constraints += obj_val[1+length(points)] >= 100*square(p_ld[2] - 2*p_ld[1] + p_ld[N]);
prob.constraints += obj_val[N+length(points)] >= 100*square(p_ld[1] - 2*p_ld[N] + p_ld[N-1]);

solver = SCSSolver(verbose=0)
solve!(prob, solver)

p_ld = p_ld.value

# Plot the curve
if PLOT_FIGURES
    figure(figsize=fig_size)
    plot(p_ld)
    title("Load Curve (kW)", fontsize=19)
    ylabel("Power (kW)")
    xticks(xtick_vals, xtick_labels )
end;


# # For reference, plot the net load curve: load - solar
# # Aside: the shape of this curve is referred to as "the duck curve"
# # by some people in energy (since the shape looks like a duck on profile), and
# # is a result of renewable generation displacing load demand in the day.
# if PLOT_FIGURES
#     figure(figsize=fig_size)
#     plot(p_ld - p_pv)
#     axhline(0, color="black", linestyle="--")
#     title("Load minus Solar (kW)", fontsize=19)
#     ylabel("Power (kW)")
#     xticks(xtick_vals, xtick_labels )
#     show()
# end

#############################################
# Battery and Grid Line Constraint Values
#############################################
# Max charge and discharge rates
D = 10;   # Max discharge rate (kW)
C = 8;    # Max charge rate (kW)
Q = 27;   # Max energy (kWh)

# Final list of values generated:
# N (scalar): number of intervals we split the day into
# R_buy (vector, $/kWh): prices one can buy energy at from grid in given interval
# R_sell (vector, $/kWh): prices one can sell energy at to grid in given interval
# p_pv (vector, kW): power generated by solar
# p_ld (vector, kW): power demands of load
# D (scalar, kW): max discharge rate of battery
# C (scalar, kW): max charge rate of battery
# Q (scalar, kWh): max energy of battery