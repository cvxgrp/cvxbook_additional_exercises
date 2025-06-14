#read in image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

img = mpimg.imread("../figures/flower.png")
img = img[:,:,0:3]
m,n,_ = img.shape

np.random.seed(5)
random_numbers = np.random.rand(m,n)
known_ind = np.where(random_numbers >= 0.90)

# Very important as of 2025. Without this the solvers 
# declare the problem as primal infeasible due to numerics.
img = img.astype('float64')

# grayscale image
M = 0.299*img[:,:,0]+0.587*img[:,:,1]+0.114*img[:,:,2]
# known color values
R_known = img[:,:,0]
G_known = img[:,:,1]
B_known = img[:,:,2]
R_known = R_known[known_ind]
G_known = G_known[known_ind]
B_known = B_known[known_ind]

def save_img(filename, R,G,B):
   img = np.stack((np.array(R),np.array(G),np.array(B)), axis=2)
   plt.imshow(img)
   plt.axis('off')  # Turn off axis labels and ticks
   plt.gca().xaxis.set_major_locator(plt.NullLocator())  # Remove x-axis ticks
   plt.gca().yaxis.set_major_locator(plt.NullLocator())  # Remove y-axis ticks
    
   plt.savefig(filename, bbox_inches='tight', pad_inches=0)

R_given = np.copy(M)
R_given[known_ind] = R_known
G_given = np.copy(M)
G_given[known_ind] = G_known
B_given = np.copy(M)
B_given[known_ind] = B_known
save_img("flower_2025_given.png", R_given, G_given, B_given)
