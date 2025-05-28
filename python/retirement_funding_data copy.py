import numpy as np
import matplotlib.pyplot as plt
# Parameters
T = 30  # Retiree's life expectancy post retirement (in years)
# Initial account balances (in thousands $)
B_init = 800.0
I_init = 800.0
R_init = 400.0
# Investment returns (inflation adjusted)
rho_B = 1.05
rho_I = 1.05
rho_R = 1.05
# Required Minimum Distribution fractions for 2024
# https://smartasset.com/retirement/rmd-table
kappa = np.zeros(T)
ages = np.arange(65, 65 + T)
distribution_periods = {
    72: 27.4, 73: 26.5, 74: 25.5, 75: 24.6, 76: 23.7,
    77: 22.9, 78: 22.0, 79: 21.1, 80: 20.2, 81: 19.4,
    82: 18.5, 83: 17.7, 84: 16.8, 85: 16.0, 86: 15.2,
    87: 14.4, 88: 13.7, 89: 12.9, 90: 12.2, 91: 11.5,
    92: 10.8, 93: 10.1, 94: 9.5}
for t in range(T):
    age = ages[t]
    if age >= 72:
        y_t = distribution_periods[age]
        kappa[t] = 1 / y_t
# Adjusted tax brackets and marginal rates for single individuals
# https://www.irs.gov/newsroom/irs-provides-tax-inflation-adjustments-for-tax-year-2024
K = 5
beta = [11.6, 47.150, 100.525, 191.950, 243.725]
eta = [0.10, 0.12, 0.22, 0.24, 0.32, 0.35]

def find_phi_beta(beta, eta, K):
  phi_beta = [0.0]
  beta = np.insert(beta, 0, 0.0)
  for k in range(1, K + 1):
      phi_k = phi_beta[k - 1] + eta[k - 1] * (beta[k] - beta[k - 1])
      phi_beta.append(phi_k)
  return phi_beta

def phi(omega, beta, eta, phi_beta, K):
  beta = np.insert(beta, 0, 0.0)
  for k in range(K):
      if omega <= beta[k + 1]:
          return phi_beta[k] + eta[k] * (omega - beta[k])
  return phi_beta[-1] + eta[-1] * (omega - beta[-1])


def plot_optimal_account_values(B, I, R):
  ages = np.arange(65,65+len(B))
  plt.figure(figsize=(10, 6))
  plt.stackplot(ages, 
                B, I, R, 
                labels=[r'$B_t^\star$', 
                        r'$I_t^\star$', 
                        r'$R_t^\star$'])
  plt.xlabel('Age (years)')
  plt.ylabel(r'Account values (in $1000)')
  plt.legend()
  plt.grid(False)
  plt.tight_layout()
  plt.savefig('optimal_account_values.pdf')
  plt.show()

def plot_optimal_withdrawal_amounts(b,i,r):
  np.arange(65,65+len(b))
  plt.figure(figsize=(10, 6))
  plt.plot(ages, b, label = r'$b_t^\star$')
  plt.plot(ages, i, label = r'$i_t^\star$')
  plt.plot(ages, r, label = r'$r_t^\star$')
  plt.xlabel('Age (years)')
  plt.ylabel(r'Withdrawals (in $1000)')
  plt.legend()
  plt.grid(False)
  plt.tight_layout()
  plt.savefig('optimal_withdrawal_amounts.pdf')
  plt.show()

def plot_roth_conversion(roth_conversion):
  np.arange(65,65+len(roth_conversion))
  plt.figure(figsize=(10, 6))
  plt.plot(ages, roth_conversion, color = "black")
  plt.xlabel('Age (years)')
  plt.ylabel(r'Roth conversion (in $1000)')
  plt.grid(False)
  plt.tight_layout()
  plt.savefig('roth_conversion.pdf')
  plt.show()

def plot_taxable_income(omega):
  beta = [11.6, 47.150, 100.525, 191.950, 243.725]
  np.arange(65,65+len(omega))
  plt.figure(figsize=(10, 6))
  plt.plot(ages, omega, color = "black")
  for j in range(len(beta)):
    plt.axhline(beta[j], color = "gray", linestyle = "dashed")
  plt.xlabel('Age (years)')
  plt.ylabel(r'Taxable income (in $1000)')
  plt.grid(False)
  plt.tight_layout()
  plt.savefig('taxable_income.pdf')
  plt.show()

# The function "plot_phi" is not needed for the assigment
def plot_phi(beta, eta, K):
  omega_vals = np.linspace(0, 280, 1000)
  phi_beta = find_phi_beta(beta, eta, K)
  phi_vals = [phi(omega, beta, eta, phi_beta, K) for omega in omega_vals]

  plt.figure(figsize=(10, 6))
  plt.plot(omega_vals, phi_vals, color='black')
  for b in beta:
      plt.axvline(x=b, color='gray', linestyle='--')
  plt.xlabel(r'$\omega$')
  plt.ylabel(r'$\phi(\omega)$')
  plt.grid(False)
  plt.tight_layout()
  plt.savefig('phi.pdf')
  plt.show()

# The function "plot_kappa" is not needed for the assigment
def plot_kappa(kappa):
  ages = np.arange(65,65+len(kappa))
  plt.figure(figsize=(10, 6))
  plt.plot(ages, kappa, color='black')
  plt.xlabel('Age (years)')
  plt.ylabel(r'$\kappa$')
  plt.grid(False)
  plt.tight_layout()
  plt.savefig('kappa.pdf')
  plt.show()

