import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img_array = mpimg.imread('demosaic_raw.png')[:,:,:3]
HEIGHT, WIDTH, _ = img_array.shape

m, n = HEIGHT, WIDTH

# Set up the masks
R_mask = np.where([[i%2==0 and j%2==0 for j in range(WIDTH)] for i in range(HEIGHT)])
G_mask = np.where([[(i%2==0 and j%2==1) or (i%2==1 and j%2==0) for j in range(WIDTH)] for i in range(HEIGHT)])
B_mask = np.where([[i%2==1 and j%2==1 for j in range(WIDTH)] for i in range(HEIGHT)])

# Load the data correctly
R_raw = np.zeros((m, n))
G_raw = np.zeros((m, n))
B_raw = np.zeros((m, n))

R_known = img_array[:,:,0]
G_known = img_array[:,:,1]
B_known = img_array[:,:,2]

R_raw[R_mask] = R_known[R_mask]
G_raw[G_mask] = G_known[G_mask]
B_raw[B_mask] = B_known[B_mask]

def save_image(R,G,B,name='output_image.png'):
    img = np.stack((np.array(R),np.array(G),np.array(B)), axis=2)
    # turn off ticks and labels of the figure
    plt.tick_params(
      axis='both', which='both', labelleft='off', labelbottom='off',
      bottom='off', top='off', right='off', left='off'
    )
    fig = plt.imshow(img)
    plt.savefig(name,bbox_inches='tight',pad_inches=0.)
