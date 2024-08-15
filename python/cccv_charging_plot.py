import numpy as np
import matplotlib.pyplot as plt

def plot_data(ax, data, y_label, color, line_label):
    ax.plot(data[:-1], color=color)
    ax.set_xlabel('Time (minute)')
    ax.set_ylabel(y_label, color=color)
    ax.tick_params(axis='y', labelcolor=color)
    ax.axhline(y=line_label, color=color, linestyle='--')

def plot_charging(i_fast, v_fast, q_fast, i_normal, v_normal, q_normal, i_slow, v_slow, q_slow, I_max, V_max, Q_max):
    plt.figure(figsize=(8, 12))
    # Fast charging plots
    ax1 = plt.subplot(3, 1, 1)
    plot_data(ax1, i_fast, 'Current (A)', 'red', I_max)
    plt.title("Fast charging")
    ax2 = plt.subplot(3, 1, 2)
    plot_data(ax2, v_fast, 'Voltage (V)', 'blue', V_max)
    ax3 = plt.subplot(3, 1, 3)
    plot_data(ax3, q_fast, 'Charge (C)', 'green', Q_max)
    plt.tight_layout()
    plt.savefig('fast_charging.pdf')
    plt.show()
    # Normal charging plots
    plt.figure(figsize=(8, 12))
    ax4 = plt.subplot(3, 1, 1)
    plot_data(ax4, i_normal, 'Current (A)', 'red', I_max)
    plt.title("Normal charging")
    ax5 = plt.subplot(3, 1, 2)
    plot_data(ax5, v_normal, 'Voltage (V)', 'blue', V_max)
    ax6 = plt.subplot(3, 1, 3)
    plot_data(ax6, q_normal, 'Charge (C)', 'green', Q_max)
    plt.tight_layout()
    plt.savefig('normal_charging.pdf')
    plt.show()
    # Slow charging plots
    plt.figure(figsize=(8, 12))
    ax7 = plt.subplot(3, 1, 1)
    plot_data(ax7, i_slow, 'Current (A)', 'red', I_max)
    plt.title("Slow charging")
    ax8 = plt.subplot(3, 1, 2)
    plot_data(ax8, v_slow, 'Voltage (V)', 'blue', V_max)
    ax9 = plt.subplot(3, 1, 3)
    plot_data(ax9, q_slow, 'Charge (C)', 'green', Q_max)
    plt.tight_layout()
    plt.savefig('slow_charging.pdf')
    plt.show()

if __name__ == "__main__":
    Q_max = 6300 
    Q_min = 960 
    R = 0.4
    a = 3.4
    b = 500
    Q_crit = 6925
    I_max = 1.5 
    V_max = 4.22 
    E = 20975
    T_fast = 120
    T_normal = 180
    T_slow = 240
    # Replace zero initialized arrays below with your solution to the problem
    #Fast charging
    i_fast = np.zeros((T_fast,))
    v_fast = np.zeros((T_fast,))
    q_fast = np.zeros((T_fast,))
    #Normal charging
    i_normal = np.zeros((T_normal,))
    v_normal = np.zeros((T_normal,))
    q_normal = np.zeros((T_normal,))
    #Slow charging
    i_slow = np.zeros((T_slow,))
    v_slow = np.zeros((T_slow,))
    q_slow = np.zeros((T_slow,))
    #Example usage
    plot_charging(i_fast, v_fast, q_fast, i_normal, v_normal, q_normal, i_slow, v_slow, q_slow, I_max, V_max, Q_max)