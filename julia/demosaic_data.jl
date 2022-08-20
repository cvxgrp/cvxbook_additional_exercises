using Images
using PyPlot

img_array = Float64.(channelview(load("demosaic_raw.png")))
img_array = img_array[1:3,:,:];

_,m,n = size(img_array);
HEIGHT, WIDTH = m, n

# Set up the masks
R_mask = find([i%2==1 && j%2==1 for i in 1:m, j in 1:n])
G_mask = find([(i%2==1 && j%2==0) || (i%2==0 && j%2==1) for i in 1:m, j in 1:n])
B_mask = find([i%2==0 && j%2==0 for i in 1:m, j in 1:n])

# Load data correctly
R_raw = img_array[1,:,:];
G_raw = img_array[2,:,:];
B_raw = img_array[3,:,:];

function save_image(R,G,B)
  plt[:ioff]()
  I = cat(3,R,G,B)
  plt[:imshow](I)
  plt[:tick_params](axis="both",which="both", labelleft="off", labelbottom="off",
                                                  bottom="off", top="off", right="off", left="off")
  plt[:savefig]("output_image.png",bbox_inches="tight",pad_inches=0.)
end
