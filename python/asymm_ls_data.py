import numpy as np

np.random.seed(0xEE364b)

n = 10
m = 100

x_true = np.random.randn(n)
noise = np.random.randn(m)
A = np.random.randn(m, n)
b = A @ x_true + noise
