import numpy as np
import matplotlib.pyplot as plt

"""t = int(input('Time(hours): '))"""

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

"""time_data = np.arange(0, t)  
power_data = []
for i in range(t):
    power_data.append(int(input('Enter power consumption for each hour: ')))

e = energy_power_consumption(time_data, power_data)

print('-=Summary=-')
print('Time data: ',t,'hour(s) in total.')
print('Power data: ',power_data,'in Watts.')
print('Energy data: ',e,'in kilo Watts per hour.')"""