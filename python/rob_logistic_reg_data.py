import numpy as np

__all__ = ['d', 'n', 'epsilon', 'X', 'y', 'X_test', 'y_test']

np.random.seed(0x364a_23F5)
d = 40
n = 60
epsilon = 0.5

true_theta = np.random.randn(d)
true_X = np.random.randn(n, d)
noise = 2 * epsilon * np.random.rand(n, d) - epsilon

X = true_X + noise
y = np.sign(true_X @ true_theta + 0.1 * np.random.rand(n) - 0.05)

true_X_test = np.random.randn(n, d)
noise = 2 * epsilon * np.random.rand(n, d) - epsilon

X_test = true_X_test + noise
y_test = np.sign(true_X_test @ true_theta + 0.1 * np.random.rand(n) - 0.05)
