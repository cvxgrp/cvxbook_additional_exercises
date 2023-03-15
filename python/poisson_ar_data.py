import numpy as np
# Set random seed for reproducibility
np.random.seed(1)
# Set initial values
num_points = 200
x = np.zeros(num_points)
lam = np.zeros(num_points)
nu = 0.3
omega = 1.5
lam[0] = nu
x[0] = np.random.poisson(lam[0])
# Generate values for x and update lambda
for t in range(1, num_points):
    lam[t] = nu*(omega**x[t-1])
    x[t] = np.random.poisson(lam[t])

def plot_x():
    """Helper function if you want to visualize x"""
    import matplotlib.pyplot as plt
    plt.stem(x)
    plt.xlabel('t')
    plt.ylabel('x')
    plt.show()
