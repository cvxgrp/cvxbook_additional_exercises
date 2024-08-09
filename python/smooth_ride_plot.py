import numpy as np
import matplotlib.pyplot as plt

# Function to plot the trajectory of the vehicle
# NOTE: This function is provided for visualization purposes only
# You do not need to understand how it works to complete the assignment
# The function takes the following inputs:
# - p: a numpy array with the position of the vehicle at each time period
# - l: a list with the positions of the green lights
# - g: a list with the time each green light turns on
# - r: a list with the time each green light turns off
# - filename: the name of the file where the plot will be saved
# The function does not return anything, 
# but it saves a plot in the file specified by the filename parameter.

def plot_trajectory(p, l, g, r, filename='smooth_ride.pdf'):
    T = len(p)
    K = len(l)
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, T+1), p, color='k', label='Position of the vehicle')
    for i in range(K):
        plt.hlines(l[i], g[i], r[i], colors='g', linestyles='solid')
        plt.vlines(g[i], 0, l[i], colors='g', linestyles='dashed')
        plt.vlines(r[i], 0, l[i], colors='g', linestyles='dashed')
        plt.hlines(l[i], 0, g[i], colors='g', linestyles='dashed')
        annotation_x = (g[i] + r[i]) / 2
        annotation_y = l[i] + 30
        plt.annotate(rf'$T_{{{i+1}}}$', (annotation_x, annotation_y), color='g', fontsize=12, ha='center')

    plt.xlabel(r'Time (seconds)')
    plt.ylabel(r'Position (meters)')
    xtick_labels = [rf'$g_{{{i+1}}}$' for i in range(K)] + [rf'$r_{{{i+1}}}$' for i in range(K)]
    xtick_positions = g + r
    ytick_labels = [rf'$l_{{{i+1}}}$' for i in range(K)]
    ytick_positions = l
    current_xticks = list(plt.xticks()[0])
    current_xtick_labels = list(plt.xticks()[1])
    new_xticks = current_xticks + xtick_positions
    new_xtick_labels = list(current_xtick_labels) + xtick_labels
    plt.xticks(new_xticks, new_xtick_labels, rotation=0)
    current_yticks = list(plt.yticks()[0])
    current_ytick_labels = list(plt.yticks()[1])
    new_yticks = current_yticks + ytick_positions
    new_ytick_labels = list(current_ytick_labels) + ytick_labels
    plt.yticks(new_yticks, new_ytick_labels)
    plt.grid(False)
    plt.xlim([0, len(p)])
    plt.ylim([0, p[-1]])
    plt.savefig(filename)
    plt.show()

if __name__ == "__main__":
    T = 301  # Total time periods (in seconds)
    K = 5  # Number of green lights
    L = 3000  # Total length of the route (in meters)
    g = [10,50,100,200,240]# Time green light turns on
    r = [40,80,130,230,270]# Time green light turns off
    l = [300,825,1620,1900,2800]# Positions of the lights (in meters)
    p = np.zeros(T) # Insert the solution of the optimization problem here
    plot_trajectory(p, l, g, r)