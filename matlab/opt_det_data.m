% data for the optimal detector design problem

rand('state',0);
n = 10; m = 6;

% create random probability distributions 
P = rand(n,m);
for i = 1:m
   P(:,i) = P(:,i)/sum(P(:,i));
end




