import numpy as np
import matplotlib.pyplot as plt

def energy_power_consumption(time_data, power_data):
    energy_data = np.cumsum(power_data) / 1000 
    fig, ax1 = plt.subplots()
    ax1.set_xlabel('Time (hours)')
    ax1.set_ylabel('Energy Consumption (kWh)', color='tab:blue')
    ax1.plot(time_data, energy_data, color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Power Consumption (W)', color='tab:red')
    ax2.plot(time_data, power_data, color='tab:red')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    plt.title('Energy and Power vs Time')
    fig.legend(['Energy','Power'])
    fig.tight_layout()
    plt.show()
    return energy_data

