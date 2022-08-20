%% data for maximizing algebraic connectivity of a graph
% provides A, F, g

rand('seed',0);
randn('seed',0);

n = 50; threshold = 0.2529;
rand('state',209);
xy = rand(n,2);

angle = 10*pi/180;
Rotate = [ cos(angle) sin(angle); -sin(angle) cos(angle) ];
xy = (Rotate*xy')';

Dist = zeros(n,n);
for i=1:(n-1);
  for j=i+1:n;
    Dist(i,j) = norm( xy(i,:) - xy(j,:) );
  end;
end;
Dist = Dist + Dist';
Ad = Dist < threshold;
Ad = Ad - eye(n);
m = sum(sum(Ad))/2;

% find the incidence matrix
A = zeros(n,m);
l = 0;
for i=1:(n-1);
  for j=i+1:n;
    if Ad(i,j)>0.5
      l = l + 1;
      A(i,l) =  1;
      A(j,l) = -1;
    end;
  end;
end;
A = sparse(A);

[n,m] = size(A);

F = ones(1,m);
g = 1;
