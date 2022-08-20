% illum_data: generates the input data for the illumination problem 
%             (a matrix A whose rows are a_k^T)

randn('seed',0);

figure(1)
L = [linspace(0,1,10); 
     1.9 1.8 1.0 1.1 1.9 1.8 1.9 1.7 1.5 1.5 ]; 

m = size(L,2);    % number of lamps

% begin and endpoints of patches 
V = [linspace(0,1,21);
    .4* [0.0 0.1 0.15 0.2 0.1 0.2 0.3 0.0 0.0 0.0 ,  ...
      0.1 0.2 0.2 0.0 0.1 0.05 0.1 0.1 0.0 0.2 0.1]];

d=plot(L(1,:), L(2,:), 'o', V(1,:), V(2,:), '-');
n = size(V,2)-1;  % number of patches

% construct A
dV = V(:,2:n+1)-V(:,1:n);    % tangent to patches
VI = V(:,1:n)+.5*dV;         % midpoint of patches
A = zeros(n,m);
for i=1:n
  for j=1:m
    dVI = L(:,j)-VI(:,i);  
    dVperp = null(dV(:,i)');  % upward pointing normal 
    if dVperp(2)<0
      dVperp = -dVperp;
    end
    A(i,j) = max(0,dVI'*dVperp/(norm(dVI)*norm(dVperp)))./norm(dVI)^2;
  end
end
