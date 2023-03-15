import numpy as np
from scipy.sparse import random as sprand
m=20
n=10
p=8
np.random.seed(2)
R = np.round(np.random.rand(m, n))
A = sprand(p, m, density=0.2).toarray()
c = 10*np.random.rand(m) + 20
b = 20*np.random.rand(p) + 30
