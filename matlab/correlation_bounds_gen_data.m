%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% clean up the workplace
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear all ; close all ; clc

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% define the data parameters
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n = 5;
m = 3;
k = 2;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% generate the problem data
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
randn('state',0);
B = randn(n,k);
Sigma0 = B*B';
A = randn(n,m);
sigma = sqrt(diag(A' * Sigma0 * A));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% find the minimum possible maximum correlation
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lb = 0;
ub = 1;
while ub-lb > 1e-6
    gamma = (lb+ub)/2;
    cvx_begin sdp quiet
        variable Sigma(n,n) symmetric
        for i = 1:(n-1)
            for j = (i+1):n
                abs(Sigma(i,j)) <= gamma * geo_mean([Sigma(i,i) , Sigma(j,j)])
            end
        end
        for i = 1:m
            A(:,i)' * Sigma * A(:,i) == sigma(i)^2
        end
        Sigma >= 0
    cvx_end
    if strcmp(cvx_status , 'Solved')
        ub = gamma;
    else
        lb = gamma;
    end
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% find a feasible Sigma
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
cvx_begin sdp quiet
    variable Sigma(n,n) symmetric
    for i = 1:(n-1)
        for j = (i+1):n
            abs(Sigma(i,j)) <= ub * geo_mean([Sigma(i,i) , Sigma(j,j)])
        end
    end
    for i = 1:m
        A(:,i)' * Sigma * A(:,i) == sigma(i)^2
    end
    Sigma >= 0
cvx_end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% construct the correlation matrix
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
gamma
Sigma
R = diag(1./sqrt(diag(Sigma))) * Sigma * diag(1./sqrt(diag(Sigma)));
rho_max = max(max(R - diag(diag(R))))

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% write the MATLAB data file
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
fid = fopen('correlation_bounds_data.m' , 'w');

fprintf(fid , 'm = %d;\n' , m);
fprintf(fid , 'n = %d;\n' , n);
fprintf(fid , 'A = ...\n[\n    ');
for i = 1:size(A,1)
    if i > 1
        fprintf(fid , ' ;\n    ');
    end
    for j = 1:size(A,2)
        if j > 1
            fprintf(fid , ' , ');
        end
        fprintf(fid , '%7.4f' , A(i,j));
    end
end
fprintf(fid , '\n];\n');

fprintf(fid , 'sigma = ...\n[\n    ');
for j = 1:length(sigma)
    if j > 1
        fprintf(fid , ' ;\n    ');
    end
    fprintf(fid , '%7.4f' , sigma(j));
end
fprintf(fid , '\n];\n');

fclose(fid);
