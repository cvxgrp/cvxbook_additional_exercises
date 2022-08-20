import numpy as np

np.random.seed(1)
N = 100

# create an increasing input signal
xtrue = np.zeros(N)
xtrue[0:40] = 0.1
xtrue[49] = 2
xtrue[69:80] = 0.15
xtrue[79] = 1
xtrue = np.cumsum(xtrue)

# pass the increasing input through a moving-average filter 
# and add Gaussian noise
h = np.array([1, -0.85, 0.7, -0.3])
k = h.size
yhat = np.convolve(h,xtrue)
y = yhat[0:-3].reshape(N,1) + np.random.randn(N,1)

xtrue = np.asmatrix(xtrue.reshape(N,1))
y = np.asmatrix(y)
