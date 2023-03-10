import numpy as np
m = 30
n = 20
nb = 6
nh = 7
ns = 7
L = 2
sigma = .1
np.random.seed(1)
A = 0.06*np.random.normal(0, 1, size=(m, n))
Sigma = A.T@A

