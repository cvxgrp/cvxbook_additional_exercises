n = 3; m = 6; 
rand('state', 105); randn('state', 1);  
A = sprandn(n,m,0.2)*10; 
for i = 1 : m
    nz = nnz(A(:,i)); 
    if (nz ==0)
        ind = randi(n); 
        A(ind,i) = randn; 
    end
end
%A = [0 1 -1; 
%    0 4 -4; 
%    8 0 -8; 
%    0 -6 6; 
%    2 -2 0; 
%    0 2 -2]';
N = 30; 
x = [randn(m,N)]; 
[xx y] = max(A*x + 2*randn(n,N)); 
xtest = [randn(m,N)]; 
[xx ytest] = max(A*xtest+ 2*randn(n,N)); 
