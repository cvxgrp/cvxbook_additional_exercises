# affine policy.

import numpy as np
import scipy.sparse

np.random.seed(0)

m, n, p = 20, 10, 5

A = np.random.randn(m, n)
c = np.random.rand(n, 1)
b0 = np.ones((m, 1))
B = .15 * scipy.sparse.rand(m, p, .3)
