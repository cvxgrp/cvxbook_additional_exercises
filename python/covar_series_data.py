import numpy as np
np.random.seed(1)

n = 10
F = np.random.randn(10, 10)
Sigma = F.T@F
T = 10
a = np.array([0.2, 0.1, 0.2, 0.4, 0.8, 1.0, 1.0, 0.8, 0.7, 0.8])
x = np.zeros((n, T))
y = np.zeros((n, T))
for t in range(T):
    x[:, t] = np.random.multivariate_normal(np.zeros(n), a[t]*Sigma)
    y[:, t] = np.random.multivariate_normal(np.zeros(n), a[t]*Sigma)
