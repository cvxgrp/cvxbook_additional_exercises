import numpy as np
# data for censored fitting problem.
np.random.seed(15)

n = 20   # dimension of x's
M = 25   # number of non-censored data points
K = 100  # total number of points
c_true = np.random.randn(n)
X = np.random.randn(n, K)
y = X.T @ c_true + 0.1 * np.sqrt(n) * np.random.randn(K)

# Reorder measurements, then censor
sort_ind = np.argsort(y)
y = y[sort_ind]
X = X[:, sort_ind]
D = (y[M - 1] + y[M]) / 2
y = y[:M]
