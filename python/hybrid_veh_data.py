# instance of hybrid vehicle optimization problem,
# exercise 4.65 in Boyd & Vandenberghe, Convex Optimization

# fuel use is given by F(p) = p+ gamma*p^2 (for p>=0)

import numpy as np
import matplotlib.pyplot as plt

# define Preq, required power at wheels
# Preq is piecewise linear
# a is slope of each piece
a=[0.5, -0.5, 0.2, -0.7, 0.6, -0.2, 0.7, -0.5, 0.8, -0.4]
# l is length of each piece
l=[40, 20, 40, 40, 20, 40, 30, 40, 30, 60]

Preq=np.arange(a[0],a[0]*(l[0]+0.5),a[0])

for i in range(1, len(l)):
    Preq=np.r_[ Preq, np.arange(Preq[-1]+a[i],Preq[-1]+a[i]*(l[i]+0.5),a[i]) ]

#Plot required power
plt.figure()
plt.plot(list(range(Preq.size)),Preq)
plt.xlabel('time'); plt.ylabel('Preq'); plt.title('Required power')
plt.show()


T = sum(l)
Peng_max = 20.0
Pmg_min = -6.0
Pmg_max = 6.0
Ebatt_max = 100.0
eta = 0.1
gamma = 0.1
