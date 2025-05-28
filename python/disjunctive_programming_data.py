import numpy as np

np.random.seed(1111)


q = 10
k_i = 10
n = 10

R = 1
M = np.sqrt(n) * 1.1

b = np.random.randn(n)

# to get center c_ij call centers[i, j]
centers = np.random.randn(q * k_i, n)
centers = np.divide(centers, np.linalg.norm(centers, axis=1).reshape(-1, 1)) * R 
shifts = np.random.rand(q, n) * M
shifts = np.repeat(shifts, k_i, axis=0)
centers += shifts
centers = centers.reshape(q, k_i, n)

# to get radius r_ij call radiuses[i, j]
radiuses = (1 + np.random.rand(q, k_i)) * M
