# data for learning a quadratic metric
# provides X, Y, d, X_test, Y_test, d_test

srand(0);

n = 5;    # dimension
N = 100;  # number of distance samples
N_test = 10;

X = randn(n, N);
Y = randn(n, N);
X_test = randn(n, N_test);
Y_test = randn(n, N_test);

P_true = randn(n, n);
P_true = P_true*P_true' + eye(n);
sqrtP_true = real(sqrtm(P_true));

d = sqrt(sum((sqrtP_true*(X-Y)).^2, 1)); # exact distances
d = max(d + randn(1, N), 0);  # add noise and make nonnegative
d_test = sqrt(sum((sqrtP_true*(X_test-Y_test)).^2, 1));
d_test = max(d_test + randn(1, N_test), 0);
