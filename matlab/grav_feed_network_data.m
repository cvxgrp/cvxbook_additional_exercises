rand('state',0);
n=10;m=20;k = 3;  % (edges 1,2,3 are producers and 4 to 10 are consumers)
alpha = 15; 
Rmin = 0.5*ones(m,1); Rmax = 2.5*ones(m,1); 
Smax = 5*ones(k,1); 
L = 5*rand(m,1)+5;  %pipe length

N = 10; % 10 consumption scenarios
C=2*rand(n-k,N); % C(:,i) = c^(i) Consumption vectors

% altitudes
h = rand(n,1); 
h = sort(h, 'descend'); 

edges=[[1 1 1 2 2 2 3 3 4 4 5 5 6 6 7 7 8 7 8 9]'...
    [2 3 4 6 3 4 5 6 6 7 8 7 7 8 8 9 9 10 10 10]'];

% incidence matrix
A=zeros(n,m);
for j=1:size(edges,1)
    A(edges(j,1),j)=-1;A(edges(j,2),j)=1;
end

