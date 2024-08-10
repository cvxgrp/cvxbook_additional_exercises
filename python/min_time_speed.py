import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt
N = 50  
m = 1500  
d = 200  
h = (100 * np.sin((
    np.arange(1, N + 2) / (N + 1) * 5 * np.pi / 2 + np.pi / 4)) + 
    np.concatenate([np.zeros(10), 
                    -10 * np.arange(1, 11), 
                    6 * np.arange(1, 32) - 100])) 
eta = 0.26 * 35 * 10**6  
rho = 1.2  
A = 2.4  
c_d = 0.5 
C_D = 0.5 * rho * A * c_d
P = 1500  
F = 2 
g = 9.8
z = cp.Variable(N + 1)
f = cp.Variable(N + 1)
objective = cp.Minimize(
    cp.sum(d * cp.inv_pos(cp.sqrt(z[0:N]))))
constraints = [
    0.5 * m * z[1:N + 1] 
    + m * g * h[1:N + 1] == 0.5 * m * z[0:N] + m * g * h[0:N] 
    + eta * f[1:N + 1] - d * C_D * z[0:N],
    cp.sum(f) + 
    P / eta * cp.sum(d * cp.inv_pos(cp.sqrt(z[0:N]))) <= F,
    f >= 0,
    eta * f[0] == 0.5 * m * z[0]]
prob = cp.Problem(objective, constraints)
prob.solve()
T = prob.value
# Constant fuel burn
zc = cp.Variable(N + 1)
fc = cp.Variable()
objective = cp.Minimize(cp.sum(d * cp.inv_pos(cp.sqrt(zc[0:N]))))
constraints = [
    0.5 * m * zc[1:N + 1] 
    + m * g * h[1:N + 1] == 0.5 * m * zc[0:N] 
    + m * g * h[0:N] 
    + eta * fc - d * C_D * zc[0:N],
    (N + 1) * fc 
    + P / eta * cp.sum(d * cp.inv_pos(cp.sqrt(zc[0:N]))) <= F,
    fc >= 0,
    eta * fc == 0.5 * m * zc[0]]
prob = cp.Problem(objective, constraints)
prob.solve()
T_unif = prob.value
fig, axs = plt.subplots(3, 1, figsize=(10, 8))
axs[0].plot(np.arange(N + 1) * d, h)
axs[0].set_ylabel('Height')
axs[1].step(np.arange(N + 1) * d, np.sqrt(z.value), 'b', where='mid')
axs[1].step(np.arange(N + 1) * d, np.sqrt(zc.value), '--r', where='mid')
axs[1].legend(['Minimum time', 'Constant burn'])
axs[1].set_ylabel('Speed')
axs[2].plot(np.arange(N + 1) * d, f.value, 'b')
axs[2].plot(np.arange(N + 1) * d, fc.value * np.ones(N + 1), '--r')
axs[2].set_xlabel('Distance')
axs[2].set_ylabel('Fuel burned')
plt.tight_layout()
plt.savefig('min_time_speed.pdf')
plt.show()
