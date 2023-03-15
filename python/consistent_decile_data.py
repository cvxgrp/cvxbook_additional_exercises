import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0x364A_23F2)
N = 500
n = 10
X = np.random.uniform(low=-1, high=1, size=(N, n))
y = np.zeros(N)

_c = np.random.randn(n)
_d = np.random.randn(n)

#We generate data as gaussians with mean and variance dependent on the feature x.
for i in range(N):
    y[i] = np.random.normal(loc=_c.T @ X[i], scale=np.abs(_d.T @ X[i]))
