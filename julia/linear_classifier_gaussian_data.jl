using LinearAlgebra
using StatsPlots
using LaTeXStrings

# A list of the mu_i
# mus = [mu1,mu2,mu3,mu4,mu5]
mus = [[2. , 2.5],
    [0, 0],
    [0, -1],
    [3, 0.5],
    [8, 0]]

# A list of the Sigma_i
Sigmas = [
    [9.  0.225;
        0.225 2.25 ],
    [1. 0.8;
        0.8 2. ],
    [16. -1.6;
        -1.6  4. ],
    [4. 0.4;
        0.4 1. ],
    [1. 1.5;
        1.5 9. ]]

eta = .3

# plotting helpers 

function plot_helper(c,d; save_file="")
    """
    Takes in c and d, the parameters of the hyperplane, and plots the hyperplane
    together with the 1-sigma confidence ellipsoids for each Gaussian. 
    Provides an optional argument with a save path to save the plot, for example
    save_file="files/my_plot.pdf".
    """
    colormap=["midnightblue","blue","turquoise","lime","yellow","orange","red","deeppink"]
    covellipse(mus[1], Sigmas[1], label="", color=colormap[1])
    plot!([mus[1][1]], [mus[1][2]], markershape=:star6, label=L"$\mu_1$", color=colormap[1])
    covellipse!(mus[2], Sigmas[2], label="", color=colormap[2])
    plot!([mus[2][1]], [mus[2][2]], markershape=:star6, label=L"$\mu_2$", color=colormap[2])
    covellipse!(mus[3], Sigmas[3], label="", color=colormap[3])
    plot!([mus[3][1]], [mus[3][2]], markershape=:star6, label=L"$\mu_3$", color=colormap[3])
    covellipse!(mus[4], Sigmas[4], label="", color=colormap[4])
    plot!([mus[4][1]], [mus[4][2]], markershape=:star6, label=L"$\mu_4$", color=colormap[4])
    covellipse!(mus[5], Sigmas[5], label="", color=colormap[5])
    plot!([mus[5][1]], [mus[5][2]], markershape=:star6, label=L"$\mu_5$", color=colormap[5])

    x = [-5:.1:10...]
    y = (-c[1].*x .- d)./c[2]
    p = plot!(x,y, color=:red, aspect_ratio=:equal, legend=:topleft, label="hyperplane")

    if save_file != ""
        savefig(save_file)
    end
    return p

end