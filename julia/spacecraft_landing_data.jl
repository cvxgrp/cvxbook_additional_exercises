h = 1;
g = 0.1;
m = 10;
Fmax = 10;
p0 = [50,50,100];
v0 = [-10,0,-10];
alpha = 0.5;
gamma = 1;
K = 35;

# use the following code to plot your trajectories
# plot the glide cone (don't modify)
# Expects p in R^{K x 3} and f in R^{K x 3}
# -------------------------------------------------------
# using PyPlot
# x = LinRange(-40,55,30); 
# y = LinRange(0,55,30);
# X = repeat(x', outer=[length(x), 1]);
# Y = repeat(y, outer=[1, length(y)]);
# Z = alpha*hypot.(X,Y)
# fig = figure();
# grid(true);
# plot_surface(X, Y, Z, cmap=get_cmap("autumn"), edgecolors="k", linewidth=0.1, zorder=1, alpha=0.7);
# xlim([-40, 55]);
# ylim([0, 55]);
# zlim([0, 105]);
# ax = gca();
# ax.view_init(azim=225)

# INSERT YOUR VARIABLES HERE:
# -------------------------------------------------------
# Make sure you pass plot and quiver column vectors and
# not row vectors. To plot 3D quiver plots you need to be
# on matplotlib 1.4. Quiver plots in matplotlib are also
# specified by the location of the arrow HEADS and the
# direction, instead of the arrow base
#
# plot(p[:,1], p[:,2], p[:,3], color="blue", linewidth=2, zorder=5);
# plot the thrust profile arrows
# quiver(p[1:K,1], p[1:K,2], p[1:K,3],
#   f[:,1], f[:,2], f[:,3], zorder=5, color="black");

# Uncomment if plot doesn't show
# display(fig)
