import Gadfly: plot as gadfly_plot
import Gadfly: Theme, Geom, @colorant_str, layer
using Random
Random.seed!(1)

T = 96; # 15 minute intervals in a 24 hour period
t = 1:T;
pi = 3.14159265;
p = exp.(-cos.((t.-15)*2*pi/T) + 0.01*randn(T));
u = 2*exp.(-0.6*cos.((t.+40)*pi/T) - 0.7*cos.(t.*4*pi/T)+0.01*randn(T));

p0 = gadfly_plot(
            layer(x=t/4, y=p, Geom.path, Theme(default_color=colorant"blue")),
              layer(x=t/4, y=u, Geom.path, Theme(default_color=colorant"red")),
              );
display(p0);
