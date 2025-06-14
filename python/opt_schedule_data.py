
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

# total number of tasks
n = 10

alpha = np.random.rand(n) + 1
m = np.random.rand(n) + 1

P = [
    [0, 6], [1, 2], [1, 3], [1, 4], [1, 6],
    [2, 7], [3, 7], [3, 8], [5, 9], [6, 9], [8, 9]
]


def visualize_schedule(s, f, save=None):
    """
    Visualize a schedule.
    
    Parameters
    ----------
    s : numpy.ndarray
        Start times of tasks.
    f : numpy.ndarray
        Finish times of tasks.
    save : str, optional
        Path to save the figure.
    """
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_position([0.1, 0.1, 0.7, 0.8])
    
    # compute cost of each task
    cost = [alpha[k] / (f[k] - s[k] - m[k]) for k in range(n)]
    colorbar_max_cost = np.round(1.5 * max(cost), 1)

    # order of display of tasks
    order = np.array([0, 6, 1, 4, 5, 2, 7, 3, 8, 9])

    # plot tasks as rectangles
    for i, k in enumerate(reversed(order)):
        color = plt.cm.BuPu(cost[k] / colorbar_max_cost)
        ax.fill([s[k], f[k], f[k], s[k]], [i, i, i + 1, i + 1], color=color, edgecolor='darkblue')
        ax.text((s[k] + f[k]) / 2, i + 0.5, str(k + 1), fontsize=12, ha='center', va='center')
        
    # plot precedence constraints
    for i, j in P:
        for k in [i, j]:
            ypos = n - np.argwhere(order == k)[0, 0]
            ax.plot([f[i], f[i]], [ypos - 1, ypos], color='red', linewidth=1.5)
        
    # axes
    T = max(f)
    ax.set_xlim([0, T])
    ax.set_xticks(np.arange(0, T + 1, 5))
    ax.set_xlabel('time')
    ax.set_ylim([0, n])
    ax.set_yticks([])
    ax.set_ylabel('task')

    # colorbar
    ax_cbar = fig.add_axes([0.85, 0.1, 0.02, 0.8])
    ax_cbar.imshow(np.linspace(0, 1, 256)[:, None], aspect='auto', origin='lower', cmap='BuPu')
    ax_cbar.set_xticks([]) 
    ax_cbar.yaxis.tick_right()
    ax_cbar.set_yticks([0, 256])
    ax_cbar.set_yticklabels([0, colorbar_max_cost])
    ax_cbar.set_title('cost', fontsize=10)

    # render
    if save is not None:
        plt.savefig(save, bbox_inches='tight')
    plt.show()

