import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
from scipy.stats import multivariate_normal as normal
from matplotlib import cm

# NOTE: You just need to consider the function plot_helper(c,d,save_file=None) below
# and pass in c and d you found as its arguments. 
# No need to worry about other helper functions.

# Test line 2

def confidence_ellipse(mu,cov, ax, n_std=1.0, facecolor='none', **kwargs):
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Using a special case to obtain the eigenvalues of this
    # two-dimensionl dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)

    # Calculating the stdandard deviation of x from
    # the squareroot of the variance and multiplying
    # with the given number of standard deviations.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    # calculating the stdandard deviation of y ...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_x,mean_y = mu
    
    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)

def plot_elipses(mus,Sigmas,ax,hyp=None):
    cmap = cm.get_cmap('viridis')  #('hsv') #('nipy_spectral')
    m = len(mus)
    for i,(mu,Sigma) in enumerate(zip(mus,Sigmas)):
        confidence_ellipse(mu,Sigma, ax, n_std=1, edgecolor=cmap(i/m),lw="2")
        ax.scatter(*mus[i],label=fr"$\mu_{i+1}$",marker="*",color=cmap(i/m),zorder=20)

def generate_ellipse(corr,stds):
    return np.diag(stds)@np.array([[1,corr],[corr,1]])@np.diag(stds)

# A list of the mu_i
# mus = [mu1,mu2,mu3,mu4,mu5]
mus = [np.array([2. , 2.5]),
 np.array([0, 0]),
 np.array([ 0, -1]),
 np.array([3. , 0.5]),
 np.array([8, 0])]

# A list of the Sigma_i
Sigmas = [
    np.array([[9., 0.225],
        [0.225, 2.25 ]]),
    np.array([[1., 0.8],
        [0.8, 2. ]]),
    np.array([[16., -1.6],
        [-1.6,  4. ]]),
    np.array([[4., 0.4],
        [0.4, 1. ]]),
    np.array([[1., 1.5],
        [1.5, 9. ]])]
eta = .3

def plot_helper(c,d,save_file=None):
    """
    Takes in c and d, the parameters of the hyperplane, and plots the hyperplane
    together with the 1-sigma confidence ellipsoids for each Gaussian. 
    Provides an optional argument with a save path to save the plot, for example
    save_file="files/my_plot.pdf".
    """

    fig,ax = plt.subplots(figsize=(6,6))
    x = np.linspace(-5,10,100)
    y = (-c[0]*x - d)/c[1]
    plt.plot(x,y,color="r",linestyle="--")

    plot_elipses(mus,Sigmas,ax)
    plt.legend()
    if save_file is None:
        plt.show()
    else:
        plt.savefig(save_file)