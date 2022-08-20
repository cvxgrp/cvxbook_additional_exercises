srand(16);

m = 10;
n = 20;
p = 0.2;

x = rand(m,2);
y = rand(n,2);

Omega = rand(m,n) .> p;
Omega[1,1] = 0;
A = Omega .* (x*y');
