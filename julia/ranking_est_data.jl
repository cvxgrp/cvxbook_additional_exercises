### THIS FILE GENERATES d, K, N, N_test, TRAINING DATA X_train, pi_train, TEST DATA X_test, pi_test AND 
### THE PROJECTION FUNCTION Pi()
### YOU DO NOT NEED TO READ THIS FILE TO DO THE PROBLEM

function Pi(y)
    #=Returns the ranking of the argument.
    
    :param y: a 2d array of size N x K or a 1d array of size K, N input vectors/1 input vector to generate the rankings
    :return: a 2d array with ith row being the ranking of the ith row of y if y is a 2d array, 
    and a 1d ranking if y is a 1d array
    
    The ranking applied to the 2d array can be retrieved by y'[(+).(Pi(y), 0:size(y)[2]:length(y)-1)]
    =#
    if ndims(y) == 1
        rank = sortperm(sortperm(y));
    else
        rank = mapslices(x -> sortperm(sortperm(x)), y, dims = 2);
        end;
    return rank
    end;

# Data generation

using Random
Random.seed!(0);

N = N_test = 500;
d = 20;
K = 10;

# Generate the true theta matrix
theta_true = randn(K,d);
theta_true /= sqrt(sum(theta_true.^2));

# Sample x_i from standard Gaussian
X_test = hcat(randn(N_test,  d-1), ones(N_test, 1));
X_train = hcat(randn(N,  d-1), ones(N, 1));

# Generate the true features theta x and add noise to them
Y_train, Y_test = X_train * theta_true', X_test * theta_true';

# Add 15dB of noise to the observed y_i to generate noisy rankings
noise_snr = 15.;
sigma_noise = 10 ^ (-0.05 * noise_snr) / sqrt(K);
Y_train, Y_test = Y_train + sigma_noise * randn(N, K), Y_test + sigma_noise * randn(N_test, K);

# Get the rankins of the observed noisy data
pi_train, pi_test = Pi(Y_train), Pi(Y_test);