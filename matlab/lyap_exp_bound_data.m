% data file for Lyapunov analysis problem
clear all;
n = 5; K = 7;
randn('state', 2);
A = cell(K, 1);
for i = 1:K
    if i < 4
        AA = tril(randn(n));
    else
        AA = triu(randn(n));
    end
    A{i} = (1.1/norm(AA))*AA;
end
