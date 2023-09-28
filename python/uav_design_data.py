import numpy as np
import cvxpy as cp

K = 5    # number of missions
D = np.array([1.2e5, 4.5e5, 5.2e5, 2.4e5, 1.1e6])      # m
V = np.array([8.2e1, 5.5e1, 6.5e1, 7e1, 4.8e1])        # m/s
W_pay = np.array([2.5e1, 3.2e1, 3.2e1, 5.7e1, 9.3e0])  # kg

W_eng_min = 5      # kg
W_eng_max = 50     # kg
W_bat_min = 10     # kg
W_bat_max = 100    # kg
S_min = 8          # m^2
S_max = 30         # m^2
alpha_max = 6      # degrees

# Used specs from the below links for reference.
# (1) https://physicsworld.com/a/lithium-ion-batteries-break-energy-density-record/
# (2) https://en.wikipedia.org/wiki/Power-to-weight_ratio#Electric_motors_and_electromotive_generators
# (3) https://www2.eecs.berkeley.edu/Pubs/TechRpts/2015/EECS-2015-22.pdf
# (4) https://en.wikipedia.org/wiki/Angle_of_attack#/media/File:Coefficients_of_Drag_and_Lift_vs_AOA.jpg
# (5) https://en.wikipedia.org/wiki/Boeing_747#Specifications
W_base = 100.   # kg
CW = 5.         # dimensionless    (5)
cL = 0.08       # dimensionless    (4)
cD0 = 0.0005    # dimensionless    (4)
cD1 = 0.02      # dimensionless    (4)
CP = 0.002      # dimensionless    (2)
CE = 2.5e6      # J/kg             (1)
rho = 0.91      # kg/m^3           (3)
