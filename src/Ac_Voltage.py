import numpy as np
import matplotlib.pyplot as plt

def ac_voltage(amplitude, frequency, time, phase_shift):
    angular_frequency = 2 * np.pi * frequency
    voltage = amplitude * np.sin(angular_frequency * time + phase_shift)
    return voltage
