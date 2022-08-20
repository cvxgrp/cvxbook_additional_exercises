%clear all; close all;
rng('default'); rng(263);
n = 30;
y0 = randn(n, 1);
x = sort(1./(1+exp(-4*(y0+1)))+(1./(1+exp(-y0))+2./(1+exp(-6*(y0-2)))))-1.2;




