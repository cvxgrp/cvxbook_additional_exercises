using Convex, ECOS
using Plots
using Distributions
using Random
using StatsBase

true_mixture_weights = [.3, .5, .2];
N = 100
k = 3;

# This function generates N from the true mixture of distributions. 
# When you use this function to plot your estimated densities, 
# pass in the weights you obtain instead of the default parameters. 
function generate_samples(mixture_weights)
    Random.seed!(1)

    # Parameters for the distributions in our mixture: N(3, 2^2), U(-1, 2), L(-2, 3)
    samples = [rand(Normal(3,2), N) rand(Uniform(-1, 2), N) rand(Laplace(-2, 3), N)]
    indices = sample(1:k, Weights(mixture_weights), N)

    # Extract from each row a sample according to the corresponding index in indices
    ret = zeros(N)
    for i in 1:N
        ret[i] = samples[i, indices[i]]
    end
    return ret
end

# This function returns a matrix of dimension N x k
# Each row contains the evaluations of a datapoint under each density in the mixture. 
function evaluate_densities(samples)
    densities = zeros(length(samples), k)
    for i in 1:length(samples)
        x = samples[i]
        densities[i, :] = [pdf(Normal(3,2), x) pdf(Uniform(-1, 2), x) pdf(Laplace(-2, 3), x)]
    end
    return densities
end

# This function plots the mixture defined by the estimated mixture weights passed in
# on top of the true mixture density (true_mixture_weights is a global variable
# defined above).
function plot_estimated_and_true_density(estimated_mixture_weights)
    discretized_x = LinRange(-20, 20, 100)
    all_densities = evaluate_densities(discretized_x)
    estimated_densities = all_densities * estimated_mixture_weights
    true_densities = all_densities * true_mixture_weights
    plot(discretized_x, true_densities, label = "True")
    plot!(discretized_x, estimated_densities, label = "Estimated")
end

# The below two lines generate the samples and form the densities matrix.
# The densities matrix is of dimension N x k,
# where each row contains the evaluations of a datapoint under each density in the mixture.
samples = generate_samples(true_mixture_weights);
densities = evaluate_densities(samples);

# Plot the true and estimated densities. 
# This currently plots with some placeholder incorrect values for lambda
# You should replace these when you estimate the lambdas
display(plot_estimated_and_true_density([.1, .1, .8]))