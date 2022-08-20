using Convex
using PyPlot

# Problem data
K = 8
n = 2

# List of candidate choices as row vectors
c = [0.314 0.509; 0.185 0.282; 0.670 0.722; 0.116 0.253;
     0.781 0.382; 0.519 0.952; 0.953 0.729; 0.406 0.110]

# List of decisions. Row [i j] means c[i] preferred over c[j]
d = [1 2; 3 1; 3 2; 1 4; 2 4; 3 4; 5 1;
     5 2; 3 5; 5 4; 1 6; 6 2; 3 6; 6 4;
     5 6; 7 1; 7 2; 3 7; 7 4; 5 7; 7 6;
     1 8; 8 2; 3 8; 8 4; 5 8; 6 8; 7 8]

box = zeros(n, 2)

# Put your code for finding the bounding box here.
# box[i, 1] and box[i, 2] should be the lower and upper bounds
# of the i-th coordinate respectively.

# Drawing the bounding box
figure()
xlim(0, 1)
ylim(0, 1)
scatter(c[:,1], c[:,2])
plot([box[1,1];box[1,2];box[1,2];box[1,1];box[1,1]],
     [box[2,1];box[2,1];box[2,2];box[2,2];box[2,1]])
println("Width of bounding box = $(box[1,2] - box[1,1])")
println("Height of bounding box = $(box[2,2] - box[2,1])")

