# data and code for multiperiod portfolio rebalancing problem
import numpy as np
T = 100
n = 5
gamma = 8.0
threshold = 0.001
Sigma = np.array([[  1.512e-02,  1.249e-03,  2.762e-04, -5.333e-03, -7.938e-04],
 [  1.249e-03,  1.030e-02,  6.740e-05, -1.301e-03, -1.937e-04],
 [  2.762e-04,  6.740e-05,  1.001e-02, -2.877e-04, -4.283e-05],
 [ -5.333e-03, -1.301e-03, -2.877e-04,  1.556e-02,  8.271e-04],
 [ -7.938e-04, -1.937e-04, -4.283e-05,  8.271e-04,  1.012e-02]])
mu = np.array([ 1.02 , 1.028, 1.01 , 1.034, 1.017])
kappa_1 = np.array([ 0.002, 0.002, 0.002, 0.002, 0.002])
kappa_2 = np.array([ 0.004, 0.004, 0.004, 0.004, 0.004])

## Generate returns
# call this function to generate a vector r of market returns
generateReturns = lambda: np.random.multivariate_normal(mu,Sigma)

## Plotting code
# You must provide three objects:
# - ws: np.array of size T x n,
#       the post-trade weights w_t_tilde;
# - us: np.array of size T x n, 
#       the trades at each period: w_t_tilde - w_t;
# - w_star: np.array of size n,
#       the "target" solution w_star.
import matplotlib.pyplot as plt
colors = ['b','r','g','c','m']
plt.figure(figsize=(13,5))
for j in range(n):
    plt.plot(list(range(T)), ws[:,j], colors[j])
    plt.plot(list(range(T)), [w_star[j]]*T,  colors[j]+'--')
    non_zero_trades = abs(us[:,j]) > threshold
    plt.plot(np.arange(T)[non_zero_trades],
        ws[non_zero_trades, j], colors[j]+'o')
plt.ylabel('post-trade weights')
plt.xlabel('period $t$')
