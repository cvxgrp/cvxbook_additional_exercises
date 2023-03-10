import numpy as np

np.random.seed(364)
n = 30
y0 = np.random.randn(n, )
x = np.sort(1/(1+np.exp(-4*(y0+1)))+(1/(1+np.exp(-y0))+2/(1+np.exp(-6*(y0-2)))))-1.2