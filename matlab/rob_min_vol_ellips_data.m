% data for the robust min volume ellipsoid covering problem
n = 2;  % dimension
m = 100;  % number of data points
randn('state',0);
x=randn(n,m);
x(:,50) = 10*randn(n,1);  % add a few outliers to the set of points
x(:,80) = 10*randn(n,1);  
x(:,30) = 10*randn(n,1);  
