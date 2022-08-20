using PyPlot
using PyCall
@pyimport matplotlib.patches as patch;
n = 14;
k = 4;
lim = 10;
Cgiven = [-lim 0; 0 -lim; 0 lim; lim 0];
Rgiven = ones(k, 1) * 2;

Gindexes = [0 13; 1 7; 1 12; 2 11; 3 12; 
    4 5; 4 9; 5 8; 5 9; 5 11; 6 10; 6 12; 
    7 13; 8 13; 10 11; 10 12] + 1;

function plot_disks(C, R, Gedges, name = "disks_plot.eps")
### This function will plot the disks and the intersections.
    # Arguments
        # C : a numpy matrix with dimensions (n, 2),
        #    denoting the locations of the centers of disks.
        # R : a numpy array with dimension n,
        #    denoting the radii of disks.
        # Gedges : a list of tuples, representing the intersection
        #          constraints.
        # name : (OPTIONAL) the name of a file to save the figure.
    
    # Example Usage
    # plot_disks(C.value, R.value, Gindexes, name = "areas.png")

    # YOU DO NOT NEED TO CHANGE ANYTHING IN THIS FUNCTION.
    figure(figsize = (5, 5)); ax = axes() 
    ax[:set_xlim]([-12.5, 12.5]); ax[:set_ylim]([-12.5, 12.5]);
    for i in 1 : n
        if i <= k
            color_i = "r";
        else
            color_i = "b";
        end
        scatter(C[i,1], C[i,2], color=color_i, s=30, alpha=0.5);
        circle_i = patch.Circle((C[i,1], C[i,2]), R[i], color=color_i, fill=false);
        ax[:add_artist](circle_i)
    end
    for i in 1 : size(Gedges, 1)
        a = C[Gedges[i, 1], 1]; b = C[Gedges[i, 1], 2];
        c = C[Gedges[i, 2], 1]; d = C[Gedges[i, 2], 2];
        plot([a, c], [b, d], "k-", linewidth=1);
    end
    
    savefig(name);    
end