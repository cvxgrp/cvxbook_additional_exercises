# parameters
N = 120;
O = 60;
S = 30;
h = 0.5;
p1 = 0.3; p2 = 0.3;
pN_1 = 0.3; pN = 0.3;

### FEEL FREE TO COPY THE FOLLOWING PLOTTING CODE ### 
#figure(); ax = axes();
#x = collect(1 : N) * h;
#ax[:set_xlim]([x[1], x[N]]); ax[:set_ylim]([-1, 1]);
#plot([O * h, O * h], [0.5, 1], "r--", label="left safe region");
#plot([O * h, O * h], [-1, -0.5], "b--", label="right safe region");
#plot([S * h, S * h], [-1, 1], "k--", label="obstacle revealed");
#plot(x, P[:, 1], color="red", linewidth=2.0, label="obstacle left");
#plot(x, P[:, 2], color="blue", linewidth=2.0, label="obstacle right");
#plot(x, P[:, 3], color="green", linewidth=2.0, label="obstacle clear");
#legend(loc = 4, scatterpoints = 1); 
#savefig("path_plan_contingencies.eps");