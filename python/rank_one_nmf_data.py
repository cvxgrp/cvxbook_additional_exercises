import numpy as np

np.random.seed(seed = 16)

m = 10
n = 20
p = 0.2

x = np.random.rand(m,2)
y = np.random.rand(n,2)
Omega = np.random.rand(m,n) > p
Omega[0,0] = 0
A = Omega * x.dot(y.T)
