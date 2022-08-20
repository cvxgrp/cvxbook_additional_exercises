L = 12000;
w = [380, 520, 1560, 1710, 1820, 1880, 1930, 2000, 2050, 2100, 2140, 2150, 2200, 1135, 1243, 1351, 2300, 800, 1940];%, 5000, 3250, 1450];
q = [22, 25, 12, 14, 18, 18, 20, 10, 12, 14, 16, 18, 20,3, 5, 11, 3, 2, 5];%,33,3,4];
m = 17;
w = w(1:m);
q = q(1:m);
opts = optimoptions('intlinprog','Display','off');
cvx_solver_settings( 'cvx_slvitr', 100)

%% Generate pattern: There should be 190724 patterns;

P = [0:maxP(1)]';
for ii = 2:m
    ii/m
    maxp = maxP(ii);
    k = size(P,1);
    choices = repmat([0:maxp]', 1, k)';
    P = [repmat(P, maxp+1, 1), choices(:)];
    P = P(find(P * w(1:ii)' <= L),:); 
end
P = P(2:end,:);
n = length(P);