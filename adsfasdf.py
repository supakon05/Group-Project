import numpy as np
import matplotlib.pyplot as plt

# to calculate the alternating voltage
def alternating_voltage(amplitude, frequency, phase_shift):
    t = np.linspace(0, 1, 1000)   # a time array
    omega = 2 * np.pi * frequency   # Calculate the angular frequency
    c = np.deg2rad(phase_shift)   # Convert phase shift from degrees to radians
    voltage = amplitude * np.sin(omega * t + c)   # Calculate the voltage using the formula
    return t, voltage

# Input parameters for the alternating voltage
amplitude = float(input("Enter the amplitude of the voltage (in volts): "))
frequency = float(input("Enter the frequency of the voltage (in Hertz): "))
phase_shift = float(input("Enter the phase shift of the voltage (in degrees): "))

# Calculate the voltage and time array using the function
t, voltage = alternating_voltage(amplitude, frequency, phase_shift)

# Plot the graph
plt.plot(t, voltage)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Alternating Voltage')
plt.show()