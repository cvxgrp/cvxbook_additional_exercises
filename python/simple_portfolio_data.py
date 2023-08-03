import numpy as np

np.random.seed(1)
n = 20
pbar = np.ones(n)*.03 + np.r_[np.random.rand(n-1), np.zeros(1)]*.12
S = np.random.randn(n, n)
S = S.T @ S
S = S/max(np.abs(np.diag(S)))*.2
S[:, -1] = np.zeros(n)
S[-1, :] = np.zeros(n).T
x_unif = np.ones(n)/n
x_unit = x_unif
