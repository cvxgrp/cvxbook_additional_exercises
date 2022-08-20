N = 10; n = 100;
q = [exp(-(i - 30)^2/100) + 2 * exp(-(i - 68)^2 / 100) for i in 1:100]
r = [exp(-(i - 50)^2/100) for i in 1:100];
q /= sum(q); r /= sum(r)
