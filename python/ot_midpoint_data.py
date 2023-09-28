import numpy as np
import matplotlib.pyplot as plt

"""
Variables are:
 - k, d, n: dimensions from the problem
 - p, q: the distributions for the circle and triangle
            flattened to a vector
 - C: the cost matrix for the locations using the
            appropriate flattening that corresponds to
            p, q
 - plot_pdfs(p, q, c, optional_filename): plots
            p, q, and c

"""

__all__ = ['k', 'd', 'n', 'p', 'q', 'C', 'plot_pdfs']


k = 23; d = 2
p_square = np.zeros((k, k))
q_square = np.zeros((k, k))
for i in range(k):
    for j in range(k):
        if (i == k-d and ( d-1 <= j <= k-d)) \
            or (( d-1 <= j <= k-d) and ( d-1 <= i <= k-d) \
            and ( (i - (d - 1) - \
            np.floor((k - d - (d-1))/(d-1-(k-1)/2) * (j - (k-1)/2)) \
            in [0, -1]) or (i - (k - d) - \
                np.floor((k - d - (d-1))/(k-d-(k-1)/2) * (j - (k-d))))\
            in [0, -1])):
            q_square[i,j] = 1.
        if  (k-1)/2-d+1 <= np.sqrt((i-(k-1)/2)**2 + (j-(k-1)/2)**2) \
            <(k-1)/2-d+2:
            p_square[i,j] = 1.
q_square /= q_square.sum()
p_square /= p_square.sum()
xs = np.ones((k, 1)) @ np.arange(k).reshape(1, -1)
ys = np.arange(k).reshape(-1, 1) @ np.ones((1, k))  
points = np.stack([xs.reshape(-1), ys.reshape(-1)]).T   
diag = (np.linalg.norm(points, axis=1, ord=2)**2).reshape(k**2, 1)
# cost is l2 norm squared between 2D points
C = np.ones((k**2, 1)) @ diag.T + diag @ np.ones((1, k**2)) \
            - 2 * points @ points.T
p = p_square.flatten()
q = q_square.flatten()
n = k**2

def plot_pdfs(p, q, c, title=""):
    k = int(np.sqrt(p.size))
    p, q, c = p.reshape(k, k), q.reshape(k, k), c.reshape(k, k)
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    axes[0].matshow(p)
    axes[1].matshow(c)
    axes[2].matshow(q)
    if title:
        plt.suptitle(title)
        fig.savefig("%s.pdf"%title, bbox_inches='tight')
    plt.show()
