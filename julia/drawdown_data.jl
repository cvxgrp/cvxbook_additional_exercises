Pkg.add("DataFrames")
using DataFrames
df = readtable("asset_prices.csv");
P = convert(Array,df); # prices
T, n = size(P);
B = 1000;
asset_names = names(df); # names of assets, if you're interested.
