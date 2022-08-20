import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cvx

# This script generates data for the micro grid optimization problem
# WARNING: it imports cvxpy as cvx to generate some data, so after running it
# you might want to re-import cvxpy if you use it under a different name
# same for numpy and matplotlib.pyplot

PLOT_FIGURES = True # True to plot figures, false to suppress plots

N = 96 # Number of periods in the day (so each interval 15 minutes)

# Convenience variables for plotting
fig_size = (14,3)
xtick_vals = [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]
xtick_labels = ('0:00', '2:00am', '4:00am', '5:00am', '8:00am', '10:00am', '12:00pm', '2:00pm', '4:00pm', '6:00pm', '8:00pm', '10:00pm', '12:00am')

#############################################
# Price data generation - price values and intervals based off of PG&E Time Of Use plans
#############################################
partial_peak_start = 34   # 08:30
peak_start = 48           # 12:00
peak_end = 72             # 18:00 (6:00pm)
partial_peak_end = 86     # 21:30 (9:30pm)

off_peak_inds = np.concatenate([np.arange(partial_peak_start), np.arange(partial_peak_end, N)])
partial_peak_inds = np.concatenate([np.arange(partial_peak_start, peak_start), np.arange(peak_end, partial_peak_end)])
peak_inds = np.arange(peak_start, peak_end)

# rates in $ / kWh
off_peak_buy = 0.14
partial_peak_buy = 0.25
peak_buy = 0.45

# Rate cuts from buy prices to get sell prices
off_peak_perc_cut = 0.20
partial_peak_perc_cut = 0.12
peak_perc_cut = 0.11

off_peak_sell = (1 - off_peak_perc_cut) * off_peak_buy
partial_peak_sell = (1 - partial_peak_perc_cut) * partial_peak_buy
peak_sell = (1 - peak_perc_cut) * peak_buy

# Combine the buy and sell prices into the price vectors
R_buy = np.zeros(N)
R_buy[off_peak_inds] = off_peak_buy
R_buy[partial_peak_inds] = partial_peak_buy
R_buy[peak_inds] = peak_buy

R_sell = np.zeros(N)
R_sell[off_peak_inds] = off_peak_sell
R_sell[partial_peak_inds] = partial_peak_sell
R_sell[peak_inds] = peak_sell

# Plot the prices
if PLOT_FIGURES:
    plt.figure(figsize=fig_size)
    plt.plot(R_buy, label='Buy Price')
    plt.plot(R_sell, label='Sell Price')
    plt.legend()
    plt.ylabel('Price ($/kWh)')
    plt.title('Energy Prices ($/kWh)', fontsize=19)
    plt.xticks(xtick_vals, xtick_labels )
    plt.show()


#############################################
# Solar data generation
#############################################
# Just something simple: a shifted cosine wave, squared to smooth edges, peak at noon
shift = N / 2
p_pv = np.power(np.cos((np.arange(N) - shift) * 2 * np.pi / N), 2)

scale_factor = 35
p_pv = p_pv * scale_factor
p_pv = np.maximum(p_pv,0)
p_pv[:int(shift/2)] = 0
p_pv[-int(shift/2):] = 0

# Plot it
if PLOT_FIGURES:
    plt.figure(figsize=fig_size)
    plt.plot(p_pv)
    plt.title('PV Curve (kW)', fontsize=19)
    plt.ylabel('Power (kW)')
    plt.xticks(xtick_vals, xtick_labels )
    plt.show()


#############################################
# Load Data Generation (using cvx)
#############################################
# Fit a curve to some handpicked points and constrain the end points
# to match and the derivative at the end to be the same at the beginning

# points to fit to
points = [
    [0, 7],
    [10, 8],
    [20, 10],
    [28, 15],
    [36, 21],
    [45, 23],
    [52, 21],
    [56, 18],
    [60, 22.5],
    [66, 24.3],
    [70, 25],
    [73, 24],
    [83, 19],
    [95, 7],
]
points = np.array(points)

# Formulate an optimization problem that minimizes the error of 
# the fit while also minimizing the 2nd order difference of the function
p_fit = cvx.Variable(N)
obj_val = 0
# Add periodicity constraints
constr = [p_fit[0] == p_fit[-1]] # Constraint the end points to match
constr += [(p_fit[1] - p_fit[0]) == (p_fit[-1] - p_fit[-2])] # constraint deriv at endpoints to match
# Loss for fitting the data points
for pt in points:
    obj_val += cvx.square(p_fit[pt[0]] - pt[1])

# Loss for 2nd order smoothness (weight parameter chosen from weight twiddling)
for i in range(N):
    obj_val += 100*cvx.square(p_fit[(i+1) % N] - 2*p_fit[i] + p_fit[(i-1) % N])
    
obj = cvx.Minimize(obj_val)
prob = cvx.Problem(obj, constr)
prob.solve()
p_fit = p_fit.value
p_ld = p_fit

# Plot the curve
if PLOT_FIGURES:
    plt.figure(figsize=fig_size)
    plt.plot(p_fit)
#    plt.plot(points[:,0], points[:,1], 'o') # For plotting the interpolation points
    plt.title('Load Curve (kW)', fontsize=19)
    plt.ylabel('Power (kW)')
    plt.xticks(xtick_vals, xtick_labels )
    plt.show()


# For reference, plot the net load curve: load - solar
# Aside: the shape of this curve is referred to as "the duck curve"
# by some people in energy (since the shape looks like a duck on profile), and
# is a result of renewable generation displacing load demand in the day.
if PLOT_FIGURES:
    plt.figure(figsize=fig_size)
    plt.plot(p_ld - p_pv)
    plt.axhline(0, color='black', linestyle='--')
    plt.title('Load minus Solar (kW)', fontsize=19)
    plt.ylabel('Power (kW)')
    plt.xticks(xtick_vals, xtick_labels )
    plt.show()


#############################################
# Battery and Grid Line Constraint Values
#############################################
# Max charge and discharge rates
D = 10   # Max discharge rate (kW)
C = 8    # Max charge rate (kW)
Q = 27   # Max energy (kWh)

'''
Final list of values generated:

N (scalar): number of intervals we split the day into
R_buy (vector, $/kWh): prices one can buy energy at from grid in given interval
R_sell (vector, $/kWh): prices one can sell energy at to grid in given interval
p_pv (vector, kW): power generated by solar
p_ld (vector, kW): power demands of load
D (scalar, kW): max discharge rate of battery
C (scalar, kW): max charge rate of battery
Q (scalar, kWh): max energy of battery
'''
