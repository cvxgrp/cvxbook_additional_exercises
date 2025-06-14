#read in imgage
using Images, PyPlot
srand(2)
img = data(separate(load("../figures/flower.png")))
img = img[:,:,1:3];
m,n,_ = size(img);
known_ind = find(rand(m,n) .>= 0.90);
# grayscale image
M = 0.299*img[:,:,1]+0.587*img[:,:,2]+0.114*img[:,:,3];
# known color values
R_known = img[:,:,1];
G_known = img[:,:,2];
B_known = img[:,:,3];
R_known = R_known[known_ind]; 
G_known = G_known[known_ind]; 
B_known = B_known[known_ind];

function save_img(filename, R,G,B)
  plt[:ioff]()
  I = cat(3,R,G,B)
  plt[:imshow](I)
  plt[:tick_params](axis="both",which="both", labelleft="off", labelbottom="off",
    bottom="off", top="off", right="off", left="off")
  plt[:savefig](filename,bbox_inches="tight",pad_inches=0.)
end

R_given = copy(M);
R_given[known_ind] = R_known;
G_given = copy(M);
G_given[known_ind] = G_known;
B_given = copy(M);
B_given[known_ind] = B_known;
save_img("flower_given.png", R_given, G_given, B_given)
