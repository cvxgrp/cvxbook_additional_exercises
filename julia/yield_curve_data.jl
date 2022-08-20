T = 120; t = collect(1:120); 
y_true = 0.0006 * log.(3 + t) + 0.0007;
p_true = [1; (y_true + 1) .^ (- t)]
F = 1000  # face value
K = 9     # 9 different bonds 
T = 120   # 120 months (10 years)
r = 0.05; # interest rate (could change depending on maturity)
# constructing coupons 
C = zeros(K, T); # matrix of bond coupons (rows = bonds, columns = coupon payments)
C[1, 24] = F             # bond 1: zero coupon, 2 year maturity 
C[2, 60] = F             # bond 2: zero coupon, 5 year maturity 
C[3, 120] = F            # bond 3: zero coupon, 10 year maturity
C[4, (0:6:24)[2:end]] = r * F / 2; C[4, 24] += F   # bond 4: semi-annual cpn, 2 yr maturity
C[5, (0:6:60)[2:end]] = r * F / 2; C[5, 60] += F   # bond 5: semi-annual cpn, 5 yr maturity 
C[6, (0:6:120)[2:end]] = r * F/ 2; C[6, 120] += F  # bond 6: semi-annual cpn, 10 yr maturity
C[7, (0:3:24)[2:end]] = r * F/ 4; C[7, 24] += F    # bond 7: quarterly cpn, 2 yr maturity
C[8, (0:3:60)[2:end]] = r * F/ 4; C[8, 60] += F    # bond 8: quarterly cpn, 5 yr maturity
C[9, (0:3:120)[2:end]] = r * F/ 4; C[9, 120] += F; # bond 9: quarterly cpn, 10 yr maturity
C = [zeros(K) C]; # adding t = 0
# 'true' prices
b = C * p_true
