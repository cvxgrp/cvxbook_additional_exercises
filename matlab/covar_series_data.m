rng('default');
rng(2);

n = 10;
F = rand(10, 10);
Sigma = F'*F;
T = 10;
a = [0.2, 0.1, 0.2, 0.4, 0.8, 1.0, 1.0, 0.8, 0.7, 0.8];
x = zeros(n, T);
y = zeros(n, T);
for t = 1:T
    x(:, t) = mvnrnd(zeros(1,n), a(t)*Sigma);
    y(:, t) = mvnrnd(zeros(1,n), a(t)*Sigma);
end
