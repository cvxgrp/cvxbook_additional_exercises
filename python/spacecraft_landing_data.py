import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

h = 1.
g = 0.1
m = 10.
Fmax = 10.
p0 = np.matrix('50 ;50; 100')
v0 = np.matrix('-10; 0; -10')
alpha = 0.5
gamma = 1.
K = 35

# use the following code to plot your trajectories
# and the glide cone (don't modify)
# -------------------------------------------------------
# fig = plt.figure()
# ax = fig.gca(projection="3d")
# X = np.linspace(-40, 55, num=30)
# Y = np.linspace(0, 55, num=30)
# X, Y = np.meshgrid(X, Y)
# Z = alpha*np.sqrt(X**2+Y**2)
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.autumn, linewidth=0.1, alpha = 0.7, edgecolors="k")
# ax = plt.gca();
# ax.view_init(azim=225)
# #Have your solution be stored in p
# ax.plot(xs=p.value[0,:],ys=p.value[1,:],zs=p.value[2,:], c='b', lw=2, zorder = 5)
# ax.quiver(p.value[0,:-1],p.value[1,:-1],p.value[2,:-1], 
#          f.value[0,:], f.value[1,:], f.value[2,:], zorder=5, color="black")
# 
# ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
# plt.show()
