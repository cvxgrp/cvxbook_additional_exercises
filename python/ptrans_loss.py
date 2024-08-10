import cvxpy as cp
import numpy as np
from ptrans_loss_data import A, a, b, Gmax, L, l, Rmax, Rmin
from ptrans_loss_data import R, sigma, Vmax, alpha, k, m, n
Ap = np.maximum(A, 0)
Am = np.maximum(-A, 0)
# Parts a and b
p_in = cp.Variable(m)
p_out = cp.Variable(m)
g = cp.Variable(k)
lambda_ = cp.Variable(n - k)
objective = cp.Minimize(a.T @ g 
                        + cp.sum(cp.multiply(b, g**2)))
constraints = [
    p_in <= sigma * (R**2),
    p_in >= 0,
    p_out >= 0,
    g <= Gmax,
    g >= 0]
for j in range(m):
    constraints.append(
        p_in[j] >= p_out[j] 
        + alpha * L[j] / (R[j]**2) * p_out[j]**2)
constraints.append(Ap[:k, :] @ p_out + g == Am[:k, :] @ p_in)
constraints.append(Ap[k:n, :] @ p_out == Am[k:n, :] @ p_in + l)
problem = cp.Problem(objective, constraints)
problem.solve()
lambda_.value = constraints[-1].dual_value
pinUnif = p_in.value
poutUnif = p_out.value
gUnif = g.value
valUnif = problem.value
marginalUnif = lambda_.value
# Part c: Optimization with variable conductor radii
s = cp.Variable(m)
lambda_ = cp.Variable(n - k)
objective = cp.Minimize(a.T @ g + cp.sum(cp.multiply(b, g**2)))
constraints = [
    p_in <= sigma * s,
    p_in >= 0,
    p_out >= 0,
    g <= Gmax,
    g >= 0,
    s <= Rmax**2,
    s >= Rmin**2,
    L.T @ s <= Vmax]
for j in range(m):
    constraints.append(
        p_in[j] >= p_out[j] 
        + alpha * L[j] * cp.quad_over_lin(p_out[j], s[j]))
constraints.append(Ap[:k, :] @ p_out + g == Am[:k, :] @ p_in)
constraints.append(Ap[k:n, :] @ p_out == Am[k:n, :] @ p_in + l)
problem = cp.Problem(objective, constraints)
problem.solve()
lambda_.value = constraints[-1].dual_value
pinOpt = p_in.value
poutOpt = p_out.value
gOpt = g.value
valOpt = problem.value
marginalOpt = lambda_.value
Ropt = np.sqrt(s.value)
print(f"We find that the optimal cost of power generation 
      for the unoptimized network is {valUnif:.2f} and 
      the optimal cost of power generation 
      for the optimized network is {valOpt:.2f}.")
print("The marginal cost of load powers for the unoptimized network are:")
marginalUnif_rounded = np.round(marginalUnif, 4)
print(marginalUnif_rounded)
print("While the network optimized marginal costs are:")
marginalOpt_rounded = np.round(marginalOpt, 4)
print(marginalOpt_rounded)
print("Lastly, the unoptimized radii R vs the optimized radii Ropt are:")
R_vs_Ropt = np.column_stack((R, Ropt))
R_vs_Ropt_rounded = np.round(R_vs_Ropt, 4)
print(R_vs_Ropt_rounded)