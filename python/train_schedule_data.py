##################################################################
#### This data will be given, i.e. train_timetable_data.py #######
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D

######################### Problem data #########################
# Routes

K = 15 # total number of trains
S = 20 # total number of stops

d = [[129.11, 138.19, 128.89, 138.86, 132.84, 134.56, 136.72, 133.26, 130.16, 128.63, 127.13, 136.34, 132.18, 128.22, 138.32, 129.84, 131.80, 130.15, 134.80],
    [134.12, 134.40, 129.72, 129.99, 129.55, 130.59, 128.02, 128.32, 139.50, 139.44, 128.64, 126.34, 128.86, 135.80, 136.91, 126.32, 134.09, 126.02, 133.22],
    [134.96, 139.80, 129.63, 137.23, 138.19, 138.92, 126.03, 132.57, 139.74, 131.59, 137.39, 133.65, 136.79, 132.79, 126.41, 127.21, 127.56, 129.52, 139.51],
    [134.84, 137.43, 133.93, 134.89, 137.37, 138.97, 138.78, 137.55, 127.32, 131.05, 126.50, 133.65, 137.15, 126.72, 128.64, 131.12, 129.42, 137.13, 130.93],
    [134.94, 132.91, 134.17, 139.15, 139.21, 127.56, 137.81, 130.84, 127.41, 131.37, 133.14, 139.46, 131.20, 126.17, 138.04, 127.56, 132.70, 137.90, 133.21],
    [132.25, 137.21, 126.29, 134.02, 131.76, 139.79, 137.22, 126.76, 128.67, 132.33, 135.84, 130.65, 131.04, 138.90, 139.35, 131.71, 138.58, 130.62, 127.16],
    [133.37, 135.25, 138.50, 139.51, 136.78, 136.63, 135.94, 135.82, 136.74, 139.64, 131.23, 127.16, 129.35, 129.10, 131.09, 137.34, 126.84, 132.30, 137.38],
    [129.70, 126.89, 129.39, 127.19, 137.31, 128.38, 128.73, 137.40, 137.34, 134.25, 138.81, 126.84, 139.51, 133.99, 130.24, 137.56, 135.23, 139.81, 127.50],
    [134.13, 132.62, 135.13, 129.39, 126.44, 133.62, 131.11, 138.49, 132.43, 131.86, 134.86, 133.38, 139.46, 137.05, 132.95, 128.96, 134.46, 136.48, 136.58],
    [139.91, 129.06, 131.96, 131.93, 130.46, 131.11, 132.69, 133.59, 129.71, 127.88, 130.23, 127.91, 130.45, 135.51, 134.42, 139.96, 133.85, 133.68, 134.99],
    [136.18, 134.62, 134.24, 134.47, 130.97, 136.88, 134.46, 130.33, 129.44, 127.00, 130.87, 126.18, 128.32, 126.85, 129.89, 130.88, 134.28, 136.85, 134.75],
    [128.24, 138.51, 136.23, 132.97, 135.01, 133.13, 128.35, 134.98, 139.83, 136.78, 128.54, 127.68, 139.02, 138.74, 136.49, 136.65, 128.00, 137.37, 128.69],
    [128.17, 131.70, 126.01, 137.84, 128.26, 136.35, 134.16, 136.78, 134.40, 139.46, 131.32, 132.96, 130.74, 136.40, 130.21, 137.18, 127.20, 129.30, 132.13],
    [127.76, 128.84, 137.78, 131.21, 129.06, 137.85, 134.06, 134.87, 138.44, 136.00, 129.71, 126.14, 133.69, 135.91, 137.28, 128.67, 134.88, 139.14, 129.61],
    [130.09, 131.96, 134.00, 139.86, 134.23, 138.43, 135.19, 132.62, 130.28, 130.90, 136.88, 128.49, 127.93, 128.98, 135.36, 131.20, 128.89, 130.63, 127.14]]

d = np.matrix(d)

# Connections
C = [(0, 4, 2, 3),
     (0, 3, 3, 3),
     (0, 6, 6, 7),
     (0, 18, 1, 18),
     (1, 16, 2, 16),
     (1, 10, 4, 10),
     (1, 15, 3, 15),
     (2, 2, 3, 4),
     (2, 2, 4, 2),
     (2, 4, 5, 4),
     (2, 13, 5, 13),
     (2, 17, 5, 17),
     (3, 9, 4, 11),
     (4, 15, 5, 15),
     (5, 2, 11, 3),
     (4, 4, 5, 2),
     (5, 5, 8, 7),
     (6, 4, 7, 5),#
     (6, 6, 10, 8),
     (6, 13, 9, 13),
     (7, 4, 9, 4),#
     (7, 10, 6, 10),
     (7, 11, 8, 11),
     (4, 12, 6, 11),
     (6, 2, 9, 2),#
     (11, 13, 13, 12),
     (8, 16, 6, 16),
     (9, 9, 11, 10),
     (8, 9, 9, 10),
     (9, 17, 11, 18),
     (10, 12, 11, 14),
     (10, 16, 13, 15),
     (13, 14, 8, 14),
     (11, 5, 14, 5),
     (14, 6, 10, 6),
     (12, 1, 10, 1),
     (13, 2, 14, 2),
     (13, 10, 11, 11),
     (14, 14, 5, 12),
     (14, 15, 9, 15)]

tau_min = 8 # stop 8 minutes at each station
T_min = 4 # minimum connection time : 4 min

v_min = 4 # 4.5km / min
v_max = 5.5 # 5km / min
# given first station arrival time = 0 (starts at 0:00)
T_start = 0 
# given last arrival time vector (720 (min) refers to after 12 hours) 
T_end = [716, 718, 716, 708, 720, 714, 714, 706, 714, 708, 706, 700, 710, 714, 710]

################ schedule draw helper function ####################
def scheduleDraw(A, D, C):
    f = plt.figure(figsize=(20, 5))
    for i in range(K):
        # Train line
        someY = i+1
        
        # start
        plt.plot(A[i,0]*np.ones(1000), 
                 np.linspace(someY-0.2, someY+0.2, 1000), "r-")
        
        # transit
        currentAxis = plt.gca()
        for s in range(S-1):
            x = (D[i,s] + A[i,s])/2
            #print("center is", x)
            width = D[i,s] - A[i,s]
            #print("width is", width)
            height = 0.4
            currentAxis.add_patch(Rectangle((x - width/2, someY - .2), 
                                            width, height, alpha=1))

        # final destination
        x = (720 + A[i,-1])/2
        width = 720 - A[i,-1]
        currentAxis.add_patch(Rectangle((x - width/2, someY - .2), 
                                        width, height, alpha=1, color="y"))
        # T_end
        plt.plot(A[i,-1]*np.ones(1000), 
                 np.linspace(someY-0.2, someY+0.2, 1000), 
                 color ="c", linestyle="-")
    
    for c in C:
        k, s, k_p, s_p = c
        minDes = np.minimum(D[k,s], D[k_p, s_p])
        maxArr = np.maximum(A[k,s], A[k_p, s_p])
        if minDes - maxArr > 0:
            plt.plot(minDes*np.ones(1000), np.linspace((k+1)-0.2, 
                     (k_p+1)+0.2, 1000), "g--")
            plt.plot(maxArr*np.ones(1000), np.linspace((k+1)-0.2, 
                     (k_p+1)+0.2, 1000), "g--")
    
    plt.xlim([-5, 720])
    plt.ylim([0,K+0.5])
    plt.ylabel(r"Train $k$")
    plt.xlabel(r"Time, $t$ (minutes)")
    plt.title("Schedule")

    yellow_patch = mpatches.Patch(color='y', label='destination')
    green_line = Line2D([0], [0], color='g', linewidth=2, 
                        linestyle='--', label="connection")
    red_line = Line2D([0], [0], color='r', linewidth=2, 
                        linestyle='-', label="start")
    c_line = Line2D([0], [0], color='c', linewidth=2, 
                        linestyle='-', label="final arrival")

    plt.legend(handles=[yellow_patch, green_line, red_line, c_line],
               loc='upper center', bbox_to_anchor=(0.5, -0.15),
               fancybox=True, shadow=True, ncol=4)
    return f
##################################################################

######### plot connection time histogram (distribution) ########
def get_hist(A, D, C):
    arr = []
    for c in C:
        k, s, k_p, s_p = c
        minDes = np.minimum(D[k,s], D[k_p, s_p])
        maxArr = np.maximum(A[k,s], A[k_p, s_p])
        if minDes - maxArr > 0:
            arr.append(minDes - maxArr)
    return arr
