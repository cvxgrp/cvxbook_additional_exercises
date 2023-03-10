import numpy as np

rng = np.random.Generator(np.random.MT19937(seed=12345))
n = 20
# _A and _C are internal - you don't need them.
_A = rng.standard_normal((2*n, n))
_C = np.diag(0.5*np.exp(rng.standard_normal((n,))))

Sigma = _C@_A.T@_A@_C
Sigma = 0.5*(Sigma + Sigma.T)
M = np.ones(n)*0.2
sigma = np.sqrt(np.diag(Sigma))

# USE THE FOLLOWING CODE TO PLOT YOUR SOLUTION
# Replace x_max_divers and x_min_variance with your optimal values
# import matplotlib.pyplot as plt
# plt.bar(np.arange(0,20), x_max_divers, width=0.5, label="Max diversification")
# plt.bar((np.arange(0,20)*2+1)/2,   x_min_variance, width=0.5, label="Min variance")
# plt.legend()