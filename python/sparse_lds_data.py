import numpy as np
from scipy.sparse import rand as sprandn
from scipy.linalg import sqrtm

np.random.seed(123)

n = 8
A = sprandn(n, n, 0.2).todense()
A = 0.95*A/np.max(np.abs(np.linalg.eigvals(A))) # make A stable.
A = np.asmatrix(A)

m = 4
B = np.asmatrix(sprandn(n, m, 0.3).todense())

T = 100
W = np.asmatrix(np.eye(n))
Whalf = np.asmatrix(sqrtm(W))

us = np.asmatrix(10*np.random.randn(m, T-1)) #input.
ws = np.dot(Whalf, np.asmatrix(np.random.randn(n, T))) #noise process.

xs = np.asmatrix(np.zeros((n, T)))
xs[:, 0] = 50*np.random.randn(n, 1) #initial x.

# Simulate the system.
for t in range(T-1):
    xs[:, t+1] = np.dot(A, xs[:, t]) + ws[:, t] + np.dot(B, us[:, t])
