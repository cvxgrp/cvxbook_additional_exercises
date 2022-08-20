import numpy as np

n = 2
m = 100

np.random.seed(0)

x = np.random.randn(n,m)

print(x[:,49])
print(x[:,79])
print(x[:,29])

x[:,49] = 10 * np.random.randn(n)
x[:,79] = 10 * np.random.randn(n)
x[:,29] = 10 * np.random.randn(n)