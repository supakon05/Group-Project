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

def ac_voltage(amplitude, frequency, time, phase_shift):
    angular_frequency = 2 * np.pi * frequency
    voltage = amplitude * np.sin(angular_frequency * time + phase_shift)
    return voltage

print('Select an option:\n1. Energy and Power Consumption Calculator\n2. AC Voltage Calculator')
option = int(input('Choose an option: '))

if option == 1:
    t = int(input('Time (hours): '))
    time_data = np.arange(0, t)
    power_data = []
    for i in range(t):
        power_data.append(int(input(f'Enter power consumption for hour {i+1}: ')))
    e = energy_power_consumption(time_data, power_data)
    print('-=Summary=-')
    print(f'Time data: {t} hour(s) in total.')
    print(f'Power data: {power_data} in Watts.')
    print(f'Energy data: {e} in kilo Watts per hour.')
elif option == 2:
    amplitude = float(input("Enter the amplitude of the AC voltage (in volts): "))
    frequency = float(input("Enter the frequency of the AC voltage (in hertz): "))
    phase_shift = float(input("Enter the phase shift of the AC voltage (in radians): "))
    time = np.arange(0, 1, 0.01)
    voltage = ac_voltage(amplitude, frequency, time, phase_shift)
    plt.plot(time, voltage)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.title('AC Voltage')
    plt.show()
    print('-= AC Voltage Summary =-')
    print('Amplitude: ',amplitude,' volts')
    print('Frequency: ',frequency,' hertz')
    print('Phase Shift: ',phase_shift,' radians')

else:
    print('Invalid option selected.')