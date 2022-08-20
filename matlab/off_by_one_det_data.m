% data for the optimal detector design problem

rand('state',0);
n = 20; m = 5;

% create random probability distributions 
P = rand(n,m).^4;
for i = 1:m
   P(:,i) = P(:,i)/sum(P(:,i));
end
