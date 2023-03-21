import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the output voltage for an AC voltage input
def ac_voltage(amplitude, frequency, time, phase_shift):
    angular_frequency = 2 * np.pi * frequency
    voltage = amplitude * np.sin(angular_frequency * time + phase_shift)
    return voltage

# Input parameters for AC voltage calculator
amplitude = float(input("Enter the amplitude of the AC voltage (in volts): "))
frequency = float(input("Enter the frequency of the AC voltage (in hertz): "))
phase_shift = float(input("Enter the phase shift of the AC voltage (in radians): "))

# Time range for AC voltage plot
time_ac = np.arange(0, 1, 0.01)

# Calculate the output voltage for each time value
voltage_ac = ac_voltage(amplitude, frequency, time_ac, phase_shift)
# Plot the AC voltage graph
plt.plot(time_ac, voltage_ac)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('AC Voltage')
plt.show()

# Function to calculate energy and power consumption from power data over time
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
# Input parameters for energy and power consumption calculator
t = int(input('Enter total time (in hours): '))
time_data = np.arange(0, t)
power_data = []
for i in range(t):
    power_data.append(int(input('Enter power consumption for each hour: ')))

# Calculate and plot the energy and power consumption graph
energy_data = energy_power_consumption(time_data, power_data)

# Print summary of input and output data
print('-= AC Voltage Summary =-')
print('Amplitude: ',amplitude,' volts')
print('Frequency: ',frequency,' hertz')
print('Phase Shift: ',phase_shift,' radians')
print('Time data: ',t,'hour(s) in total.')
print('Power data: ',power_data,'in Watts.')
print('Energy data: ',energy_data,'in kilo Watts per hour.')