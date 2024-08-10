import numpy as np
import matplotlib.pyplot as plt

# Minimum time speed profile along a road

N = 50  # number of intervals
m = 1500  # mass of vehicle
d = 200  # distance between knot points
h = (100 * np.sin((np.arange(1, N + 2) / (N + 1) * 5 * np.pi / 2 + np.pi / 4)) + \
    np.concatenate([np.zeros(10), -10 * np.arange(1, 11), 6 * np.arange(1, 32) - 100]))  # elevation at knot points
eta = 0.26 * 35 * 10**6  # engine efficiency and energy content of the fuel

rho = 1.2  # density of air, used in calculation of C_D
A = 2.4  # effective frontal area used in calculation of C_D
c_d = 0.5  # effective aerodynamic drag coefficient NOT C_D from the problem
C_D = 0.5 * rho * A * c_d  # coefficient of drag
del rho, A, c_d

P = 1500  # power of the onboard systems
F = 2  # total initial fuel
g = 9.8  # acceleration due to gravity

# random data for initial plotting,
# you should replace these with the values you find
s = np.random.rand(N + 1)  # minimum time speed
sc = 0.2 * np.ones(N + 1)  # constant fuel speed
f = np.random.rand(N + 1)  # minimum time fuel burn
fc = 0.2 * np.ones(N + 1)  # constant fuel fuel burn

# Plotting the results
fig, axs = plt.subplots(3, 1, figsize=(10, 8))

axs[0].plot(np.arange(N + 1) * d, h)
axs[0].set_ylabel('Height')

axs[1].step(np.arange(N + 1) * d, s, 'b', where='mid')
axs[1].step(np.arange(N + 1) * d, sc, '--r', where='mid')
axs[1].legend(['Minimum time', 'Constant burn'])
axs[1].set_ylabel('Speed')

axs[2].plot(np.arange(N + 1) * d, f, 'b')
axs[2].plot(np.arange(N + 1) * d, fc, '--r')
axs[2].set_xlabel('Distance')
axs[2].set_ylabel('Fuel used')

plt.tight_layout()
plt.show()
