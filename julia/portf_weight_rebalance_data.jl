# data and code for multiperiod portfolio rebalancing problem
T = 100;
n = 5;
gamma = 8.0;
threshold = 0.001;
Sigma = [[  1.512e-02   1.249e-03   2.762e-04  -5.333e-03  -7.938e-04]
 [  1.249e-03   1.030e-02   6.740e-05  -1.301e-03  -1.937e-04]
 [  2.762e-04   6.740e-05   1.001e-02  -2.877e-04  -4.283e-05]
 [ -5.333e-03  -1.301e-03  -2.877e-04   1.556e-02   8.271e-04]
 [ -7.938e-04  -1.937e-04  -4.283e-05   8.271e-04   1.012e-02]];
mu = [ 1.02 , 1.028, 1.01 , 1.034, 1.017];
kappa_1 = [ 0.002, 0.002, 0.002, 0.002, 0.002];
kappa_2 = [ 0.004, 0.004, 0.004, 0.004, 0.004];
 
# Generate returns
# call this function to generate a vector r of market returns
using Distributions
generateReturns() = rand(MvNormal(mu, Sigma));

## Plotting code
# You must provide three objects:
# - ws: array of size T x n,
#       the post-trade weights w_t_tilde;
# - us: np.array or np.matrix of size T x n, 
#       the trades at each period: w_t_tilde - w_t;
# - w_star: np.array of size n,
#       the "target" solution w_star.
using PyPlot
figure(figsize=(13,5))
colors = ["b","r","g","c","m"];
for j = 1:n
    plot(1:T, ws[:,j], colors[j]);
    plot(1:T, w_star[j]*ones(T),  colors[j]*"--");
    non_zero_trades = abs(us[:,j]) .> threshold;
    plot((1:T)[non_zero_trades], ws[non_zero_trades,j], colors[j]*"o");
end
ylabel("post-trade weights");
xlabel("period \$t\$");
