# data for power flow problem
n = 12;     # total number of nodes
m = 18;     # number of edges (transmission lines)
k = 4;      # number of generators
Pmax = [    # transmission line capacities
    4.8005
    1.9246
    3.4274
    2.9439
    4.5652
    4.0484
    2.8259
    1.0740
    4.2856
    2.7788
    3.4617
    4.1677
    4.6873
    3.9528
    1.7051
    2.6228
    4.7419
    4.6676
];
Gmax = [3; 2; 4; 7];  # maximum generator power
c    = [4; 8; 5; 3];  # supply generator costs
d = [                 # network power demands
    1.6154
    2.3405
    1.0868
    1.5293
    2.2197
    1.0148
    1.2083
    1.3041
];
# graph incidence matrix
A = [ -1 -1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ;
       0  0 -1 -1  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ;
       0  0  0  0  0  0  0  0  0 -1 -1  0  0  0  0  0  0 -1 ;
       0  0  0  0  0  0 -1  0  0  0  0  0  0  0 -1  0 -1  0 ;
       1  0  0  0  1 -1  0  0  0  0  0  0  0  0  0  0  0  0 ;
       0  1  1  0 -1  0  1 -1  0  0  0  0  0  0  0  0  0  0 ;
       0  0  0  1  0  0  0  0 -1  1  0  0  0  0  0  0  0  0 ;
       0  0  0  0  0  0  0  1  1  0  0  0 -1  0  1  0  0  1 ;
       0  0  0  0  0  0  0  0  0  0  1 -1  0  0  0  0  0  0 ;
       0  0  0  0  0  0  0  0  0  0  0  1  1 -1  0  0  0  0 ;
       0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  1  0  0 ;
       0  0  0  0  0  1  0  0  0  0  0  0  0  0  0 -1  1  0 ];

# the code below is not data for the problem
# it is used only to generate the network graph

# x-y coordinates
XY = [      # node x-y coordinates
 1.5 5.2;   # node 1
 4.9 5;     # node 2
 6.9 3.5;   # node 3
 1.9 3.5;   # node 4
 0.2 4.4;   # node 5
 3.2 4.8;   # node 6
 5.9 4.5;   # node 7
 3.9 3.6;   # node 8
 5.9 2.5;   # node 9
 3.9 3;     # node 10
 1.4 2.5;   # node 11
 0 3];      # node 12

# node adjacency matrix
Ad = -A*A';
Ad = Ad - diagm(diag(Ad));

epsx = 0.05; epsy = 0.15; # text placing offset

using Gadfly
layers = Layer[];

# draw the edges
for i = 1:n-1
  for j = i+1:n
    if Ad[i,j] == 1
      x = [XY[i,1], XY[j,1]]
      y = [XY[i,2], XY[j,2]]
      append!(layers, layer(x=x, y=y, Geom.line, Theme(default_color=color("black"))));
    end
  end
end

# draw the nodes
append!(layers, layer(x=XY[1:k,1], y=XY[1:k,2], Geom.point, order=1,
    Theme(default_color=color("red"))));
append!(layers, layer(x=XY[k+1:end,1], y=XY[k+1:end,2], Geom.point,
    Theme(default_color=color("black"))));
graph = plot(layers, Guide.manual_color_key("", ["generator nodes", "regular nodes"],
    ["red", "black"]));
display(graph);

