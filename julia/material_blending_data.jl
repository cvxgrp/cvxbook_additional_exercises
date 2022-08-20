m = 4; # the number of raw materials
n = 2; # the number of blended materials
q = 3; # the number of constituents

# the ith column of C is c_i
C = [.9  .8  .7 .6;
     .08 .12 .2 .2;
     .02 .08 .1 .2];

# bounds on the blended product concentration
c_min = [.85 .65;
          0  0;
          0  0];
c_max = [ 1   1;
         .1  .18;
         .05 .17];

FTilde = [10;10]; # limit on the flow rate of the blended material
F = [7; 2; 6; 3]; # availibility of raw materials

p = [15; 13; 11; 8]; # price of raw materials
pTilde = [21;18]; # price of the blended material
