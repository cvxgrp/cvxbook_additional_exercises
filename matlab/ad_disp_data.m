% data for online ad display problem
rand('state',0);
n=100;      %number of ads
m=30;       %number of contracts
T=60;       %number of periods

I=10*rand(T,1);  %number of impressions in each period
R=rand(n,T);    %revenue rate for each period and ad
q=T/n*50*rand(m,1);     %contract target number of impressions
p=rand(m,1);  %penalty rate for shortfall
Tcontr=(rand(T,m)>.8); %one column per contract. 1's at the periods to be displayed
for i=1:n
	contract=ceil(m*rand);
	Acontr(i,contract)=1; %one column per contract. 1's at the ads to be displayed
end
