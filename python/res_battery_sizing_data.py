import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from datetime import datetime, timedelta

l = np.array([0.5       , 0.44647768, 0.40069089, 0.36206477, 0.33002452,
       0.30399529, 0.28340225, 0.26767058, 0.25622545, 0.24849202,
       0.24389546, 0.24186095, 0.24181365, 0.24317874, 0.24538138,
       0.24784674, 0.25      , 0.25138934, 0.25205508, 0.25216053,
       0.25186903, 0.2513439 , 0.25074846, 0.25024605, 0.25      ,
       0.25012117, 0.25051058, 0.25101681, 0.25148842, 0.25177397,
       0.25172204, 0.2511812 , 0.25      , 0.2481441 , 0.24604745,
       0.24426111, 0.2433361 , 0.24382349, 0.24627429, 0.25123957,
       0.25927035, 0.27091768, 0.28673261, 0.30726618, 0.33306942,
       0.36469338, 0.4026891 , 0.44760763, 0.5       , 0.56000115,
       0.6260816 , 0.69629574, 0.76869798, 0.84134273, 0.91228439,
       0.97957736, 1.04127605, 1.09543486, 1.14010821, 1.17335048,
       1.19321609, 1.19775945, 1.18503495, 1.153097  , 1.1       ,
       1.02790603, 0.95540779, 0.90520565, 0.9       , 0.95494199,
       1.05498593, 1.1775369 , 1.3       , 1.40376137, 1.48613134,
       1.54840128, 1.59186259, 1.61780664, 1.6275248 , 1.62230847,
       1.60344902, 1.57223783, 1.52996628, 1.47792576, 1.41740764,
       1.3497033 , 1.27610412, 1.19790149, 1.11638678, 1.03285137,
       0.94858665, 0.864884  , 0.78303478, 0.7043304 , 0.63006222,
       0.5       ])

p = np.array([0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
       0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
       0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
       0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
       0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.5,
       0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
       0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4,
       0.4, 0.4, 0.3, 0.3, 0.3])

s = np.array([2.77555756e-17, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 6.12273369e-02, 1.32675838e-01, 2.13405954e-01,
       3.02478134e-01, 3.98952829e-01, 5.01890488e-01, 6.10351562e-01,
       7.23396501e-01, 8.40085755e-01, 9.59479774e-01, 1.08063901e+00,
       1.20262391e+00, 1.32449492e+00, 1.44531250e+00, 1.56413709e+00,
       1.68002915e+00, 1.79204913e+00, 1.89925747e+00, 2.00071463e+00,
       2.09548105e+00, 2.18261719e+00, 2.26118349e+00, 2.33024041e+00,
       2.38884840e+00, 2.43606790e+00, 2.47095937e+00, 2.49258325e+00,
       2.50000000e+00, 2.49258325e+00, 2.47095937e+00, 2.43606790e+00,
       2.38884840e+00, 2.33024041e+00, 2.26118349e+00, 2.18261719e+00,
       2.09548105e+00, 2.00071463e+00, 1.89925747e+00, 1.79204913e+00,
       1.68002915e+00, 1.56413709e+00, 1.44531250e+00, 1.32449492e+00,
       1.20262391e+00, 1.08063901e+00, 9.59479774e-01, 8.40085755e-01,
       7.23396501e-01, 6.10351562e-01, 5.01890488e-01, 3.98952829e-01,
       3.02478134e-01, 2.13405954e-01, 1.32675838e-01, 6.12273369e-02,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 2.77555756e-17])

T = 96
C_max = 0.3
eta = 0.2
D = int(365*5) 
gamma = 300  

def plot_q_b_g(q_star, Q_star, b_star, B_star, g_star):
       _, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=False, sharey=False)
       times = pd.date_range(start="2022-06-01 00:00", end="2022-06-01 23:45", freq='15T')
       start_datetime = datetime(2022, 6, 1, 0, 0)
       end_datetime = datetime(2022, 6, 1, 23, 45)
       tick_hours = [0, 5, 12, 15, 16, 19, 21, 23]
       tick_times = [start_datetime + timedelta(hours=h) for h in tick_hours]
       tick_labels = [dt.strftime('%H:%M') for dt in tick_times]
       axes[0].plot(times, q_star, label=r"$q^\star$", color='black')
       axes[0].axhline(y=Q_star, color='black', linestyle='--')
       axes[0].set_ylabel("Storage (kWh)")
       axes[0].legend(loc="upper left")
       axes[0].set_xticks(tick_times)
       axes[0].set_xticklabels(tick_labels, rotation=45, ha='right')
       axes[0].set_xlim(start_datetime, end_datetime)
       axes[1].plot(times, b_star, label=r"$b^\star$", color='black')
       axes[1].axhline(y=B_star, color='black', linestyle='--')
       axes[1].axhline(y=-B_star, color='black', linestyle='--')
       axes[1].set_ylabel("Power (kW)")
       axes[1].legend(loc="upper left")
       axes[1].set_xticks(tick_times)
       axes[1].set_xticklabels(tick_labels, rotation=45, ha='right')
       axes[1].set_xlim(start_datetime, end_datetime)
       axes[2].plot(times, g_star, label=r"$g^\star$", color='black')
       axes[2].set_ylabel("Power (kW)")
       axes[2].legend(loc="upper left")
       axes[2].set_xticks(tick_times)
       axes[2].set_xticklabels(tick_labels, rotation=45, ha='right')
       axes[2].set_xlim(start_datetime, end_datetime)
       plt.tight_layout()
       plt.savefig('res_battery_sizing_solution.pdf')
       plt.show()
