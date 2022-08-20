srand(0)
n=10 ; m=20
edges=[1 1 1 2 2 2 3 3 4 4 5 5 6 6 7 7 8 7 8 9 ;
       2 3 4 6 3 4 5 6 6 7 8 7 7 8 8 9 9 10 10 10]';
A = zeros(n,m)
for j = 1:size(edges,1)
    A[edges[j,1],j] = -1
    A[edges[j,2],j] = 1
end
a = 2*rand(m,1);
x_max = 1+rand(m,1);
B=m/2;

