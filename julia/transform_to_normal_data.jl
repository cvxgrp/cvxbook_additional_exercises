srand(103)
n = 30
y0 = randn(n)
x = sort(1.0/(1+exp(-4*(y0+1)))+(1.0/(1+exp(-y0))+2.0/(1+exp(-6*(y0-2)))))-1.2;