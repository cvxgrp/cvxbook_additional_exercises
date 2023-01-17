#read in imgage
using Random, Images, Plots

function tv(R,G,B)
    m, n = size(R)
    total = 0.
    for i=1:m-1, j=1:n-1
        total += norm([R[i,j]-R[i,j+1]; R[i,j]-R[i+1,j];
                    G[i,j]-G[i,j+1]; G[i,j]-G[i+1,j];
                    B[i,j]-B[i,j+1]; B[i,j]-B[i+1,j]])
    end
    return total
end

function save_img(filename, R, G, B)
    img_colorized = RGB.(R, G, B)
    plt = plot(img_colorized, axis=:false, grid=false, ticks=false, aspectratio=1, size=(600,600))
    savefig(plt, joinpath(@__DIR__, filename))
end

Random.seed!(2)
img = load(joinpath(@__DIR__, "..", "figures", "flower.png"))

R = Float64.(red.(img))
G = Float64.(green.(img))
B = Float64.(blue.(img))
m, n = size(img);
known_ind = findall(rand(m,n) .>= 0.90);
# grayscale image
M = 0.299*R + 0.587*G + 0.114*B;
# known color values
R_known = R[known_ind]; 
G_known = G[known_ind]; 
B_known = B[known_ind];

R_given = copy(M);
R_given[known_ind] = R_known;
G_given = copy(M);
G_given[known_ind] = G_known;
B_given = copy(M);
B_given[known_ind] = B_known;
save_img("flower_given.png", R_given, G_given, B_given)
