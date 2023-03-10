import numpy as np
import matplotlib.pyplot as plt

n = 14
k = 4
lim = 10
Cgiven = np.array([[-lim, 0], [0, -lim], [0, lim], [lim, 0]])
Rgiven = [2]*k

Gindexes = np.array([
[0.000000000000000000e+00,1.300000000000000000e+01],
[1.000000000000000000e+00,7.000000000000000000e+00],
[1.000000000000000000e+00,1.200000000000000000e+01],
[2.000000000000000000e+00,1.100000000000000000e+01],
[3.000000000000000000e+00,1.200000000000000000e+01],
[4.000000000000000000e+00,5.000000000000000000e+00],
[4.000000000000000000e+00,9.000000000000000000e+00],
[5.000000000000000000e+00,8.000000000000000000e+00],
[5.000000000000000000e+00,9.000000000000000000e+00],
[5.000000000000000000e+00,1.100000000000000000e+01],
[6.000000000000000000e+00,1.000000000000000000e+01],
[6.000000000000000000e+00,1.200000000000000000e+01],
[7.000000000000000000e+00,1.300000000000000000e+01],
[8.000000000000000000e+00,1.300000000000000000e+01],
[1.000000000000000000e+01,1.100000000000000000e+01],
[1.000000000000000000e+01,1.200000000000000000e+01],
])
Gindexes = Gindexes.astype(int)

def plot_disks(C, R, Gedges, name = 'disks_plot.png'):
    '''
    This function will plot the disks and the intersections.

    # Arguments
        C : a numpy matrix with dimensions (n, 2),
        	denoting the locations of the centers of disks.
        R : a numpy array with dimension n,
        	denoting the radii of disks.
        Gedges : a list of tuples, representing the intersection
        	constraints.
        name : (OPTIONAL) the name of a file to save the figure.
    
    # Example Usage
    ``plot_disks(L.value, R.value, I, name = 'areas.png')``

    YOU DO NOT NEED TO CHANGE ANYTHING IN THIS FUNCTION.
    '''
    fig, ax = plt.subplots() 
    ax.set_aspect('equal')
    ax.set_xlim((-12.5, 12.5))
    ax.set_ylim((-12.5, 12.5))
    for i in range(0, n):
        if i < k:
            color_i = 'r'
        else:
            color_i = 'b'
        plt.scatter(C[i,0], C[i,1], c=color_i, alpha=0.5)
        circle_i = plt.Circle((C[i,0],C[i,1]), R[i], color=color_i, fill=False)
        ax.add_artist(circle_i)
    for i in range(0,len(Gedges)):
        a = C[Gedges[i, 0], 0]; b = C[Gedges[i, 0], 1];
        c = C[Gedges[i, 1], 0]; d = C[Gedges[i, 1], 1];
        plt.plot((a, c), (b, d), 'k-', linewidth=1)
    
    plt.show(); fig.savefig(name)
    return
