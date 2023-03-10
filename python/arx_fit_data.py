import numpy as np
import scipy.linalg as la
from numpy.random import RandomState
from scipy import signal

# Parameters
M = 10;
T=200;
N = 3*T;
p = 0.2;
rn = RandomState(364)

beta_true = 2*rn.rand(M)-1
beta_true = beta_true/la.norm(beta_true,1)
x_true = (rn.rand(N) < p) *rn.randn(N)

y_shifted = np.zeros(N+M);
# Shift y by M, then generate y using AR model
for t in range(N):
    y_shifted[t+M] = x_true[t]+ np.sum(np.flipud(beta_true)*y_shifted[t+M-M:t+M])
# Only observe a length T subsequence.
y= y_shifted[1+T+M:1+T+T+M]