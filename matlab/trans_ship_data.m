% optimal trans-shipment data
n = 10;
rand('state',0);
p = sort(rand(n,1));
a = rand(n,1);
d = rand(n,1);
% now get shipment costs, which need to satisfy triangle inequality.
X = rand(2,n); % random 2D locations
C=zeros(n,n);
for i=1:n
for j=1:n
C(i,j) = norm(X(:,i)-X(:,j));
end
end
