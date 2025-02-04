import numpy as np
import matplotlib.pyplot as plt

# Least-cost road grading

n = 100
d = 1  # distance between points

# Elevation of the road
e = 5 * np.sin(np.arange(1, n + 1) / n * 3 * np.pi) + np.sin(
    np.arange(1, n + 1) / n * 10 * np.pi
)

# Constraints
D1 = 0.08  # the road grade should never be greater than 8%
D2 = 0.025  # the road grade should never change faster than 25% over 10 meters
D3 = 0.005  # a further constraint on the smoothness of the road.

# Cut and fill function coefficients
alpha_fill = 2
beta_fill = 30
alpha_cut = 12
beta_cut = 1

# Plot cost functions
elevation = np.arange(0, 10.1, 0.1)
cost_fill = alpha_fill * elevation**2 + beta_fill * elevation
cost_cut = alpha_cut * elevation**2 + beta_cut * elevation

plt.figure()
plt.plot(elevation, cost_fill, "b", label="fill")
plt.plot(elevation, cost_cut, "g", label="cut")
plt.xlabel("Elevation Change")
plt.ylabel("Cost")
plt.legend()
plt.grid()
plt.savefig("road_grading_cost_function.eps")
plt.show()

if __name__ == "__main__":
    # Replace h with your solution
    h = np.ones(n) * np.mean(e)

    # Plot elevation profiles
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(np.arange(n) * d, e, "--r", label="e")
    plt.plot(np.arange(n) * d, h, "b", label="h")
    plt.ylabel("Elevation")
    plt.legend()
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(np.arange(n) * d, h - e)
    plt.ylabel("Elevation Change")
    plt.xlabel("Distance")
    plt.grid()

    plt.show()
