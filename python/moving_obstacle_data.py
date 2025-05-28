
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# dimensions and data

T, h, m, dmin = 60, 0.05, 1, 0.07
S = 1 / ((T-1) * h)

ob_p0 = np.array([
    [0.40,  0.16],
    [0.34, -0.34],
    [0.00,  0.40],
    [1.00,  0.15]
])

ob_v = np.array([
    [-0.36, -0.34],
    [ 0.00,  0.30],
    [ 0.34, -0.17],
    [-0.38, -0.09]
])

obstacles = [p0 + np.arange(T)[:, None] * h * v for p0, v in zip(ob_p0, ob_v)]  # shape (4, T, 2)


# plot

def visualize(p, save=None):
    """
    Visualize a trajectory.
    
    Parameters
    ----------
    p : numpy.ndarray
        Position, shape (T, 2).
    save : str, optional
        Path to save the GIF.
    """
                
    for t in range(T):
        _, ax = plt.figure(figsize=(6, 6)), plt.gca() 
        for ob in obstacles:
            ax.add_artist(plt.Circle(ob[t], (2/3) * dmin, color='r'))
        ax.add_artist(plt.Circle(p[t], (1/3) * dmin, color='b'))
        ax.set_xticks([0, 0.5, 1])
        ax.set_xlim(-0.1, 1.1)
        ax.set_xlabel(r'$p_x$')
        ax.set_yticks([-0.5, 0, 0.5])
        ax.set_ylim(-0.6, 0.6)
        ax.set_ylabel(r'$p_y$')
        ax.set_aspect('equal')
        ax.set_title(f'$t = {t+1}$')
        plt.savefig(f'visualization_{t}.png')
        plt.close()

    gif_duration = 3
    frame_duration = int((gif_duration / T) * 1000)
    frames = []
    for t in range(T):
        file = f'visualization_{t}.png'
        if os.path.exists(file):
            frames.append(Image.open(file))
            #os.remove(file)

    output_path = 'visualization.gif' if save is None else save
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=frame_duration,
        loop=0
    )
    print(f"GIF saved at {output_path}")
