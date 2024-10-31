import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)

# Problem data.
n = 5
m = 500
# T = 25
T = 20
M = 200
lams = np.logspace(-2, 2, 50)
# p = 0.15

# Generate training/test sets.
theta_true = np.random.randn(n,T)
X_train = np.random.randn(m,n)
t_train = np.random.choice(np.arange(1,T+1), m)
t_train = t_train - 1   # Python zero-indexing.

y_train = np.zeros(m)
y_train = np.vstack([X_train[i]*theta_true[:,t_train[i]] for i in range(m)])
y_train = y_train[:,0] + np.random.randn(m)

X_test = np.random.randn(M,n)
t_test = np.random.choice(np.arange(1,T+1), M)
t_test = t_test - 1
y_test = np.vstack([X_test[i]*theta_true[:,t_test[i]] for i in range(M)])
y_test = y_test[:,0] + np.random.randn(M)