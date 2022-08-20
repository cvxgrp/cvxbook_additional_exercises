# model-selection-cvx-data.jl
#
# Data and helper methods for the model selection problem

using PyPlot;
using LinearAlgebra;

# Regularization multiplier and values for sigma in the Kernel definition.
lambda = 1.0;
sigma_vals = [.001, .005, .01, .1, 1.0, 10.0];
d = 6;  # Length of sigma_vals

# Number of data points is m.
m = 51;
# x data points
x_data = LinRange(0, 1, m);

# y data points

y_data = [-0.0208478, 0.201887, -0.179448, 0.126084, 0.571416,
          0.498114, 0.581352, 1.161, 1.45759, 1.25205, 0.571803, 1.22437,
          1.10881, 1.13903, 0.775472, 0.935441, 1.23473, 0.976507, 0.464405,
          0.584225, 0.546602, -0.566164, 0.186539, -0.220034, 0.548431,
          -0.244135, -0.00252162, 0.175469, -0.484298, -0.729245, -0.511271,
          -0.884969, -0.959312, -1.01358, -0.396948, -1.11915, -0.951549,
          -1.01993, -0.917567, -1.09437, -0.479566, -1.60767, -0.671715,
          -0.86423, -0.460381, -0.766291, -0.391261, -0.0839596, 0.0459926,
          -0.326246, -0.0895981];

# PlotFitFromGamma(gamma; x_data, y_data, lambda, sigma_vals)
#
# Given a gamma vector solving part (d) of the problem,
# finds an appropriate dual vector that solves the Kernelized version
# of part (a) of the problem using the given x_data and y_data,
# then plots both the randomized data and the fitted line.
function PlotFitFromGamma(gamma::Vector{Float64};
                          x_data::LinRange{Float64} = x_data,
                          y_data::Vector{Float64} = y_data,
                          sigma_vals::Vector{Float64} = sigma_vals,
                          lambda::Float64 = lambda)
  # First, compute appropriate prediction for each point in x_data
  m = length(x_data);  # Number of data points in data
  d = length(sigma_vals);  # Number of kernels to use
  summed_gram_matrix = zeros(m, m);  # There are going to be d gram matrices
  X_difference_matrix = x_data * ones(1, m) - ones(m, 1) * x_data';
  for jj = 1:d
    summed_gram_matrix +=
      gamma[jj] * exp.(-abs.(X_difference_matrix) / sigma_vals[jj]);
    # gamma[jj] * exp.(-X_difference_matrix.^2 / (2 * sigma_vals[jj]^2));
  end
  # Now, given the summed gram matrix, we can easily find the optimal
  # nu for part (a). (The solutions explain this, or you could derive
  # it yourself.)
  nu_opt = (I + summed_gram_matrix / lambda) \ y_data;
  y_fitted = summed_gram_matrix * nu_opt / lambda;
  figure();
  plot(x_data, y_data, "k+");
  plot(x_data, y_fitted, "b-", linewidth=1.5);
end
