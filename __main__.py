import numpy as np
import matplotlib.pyplot as plt
from src.PowerCon import energy_power_consumption

t = int(input('Time(hours): '))

time_data = np.arange(0, t)  
power_data = []
for i in range(t):
    power_data.append(int(input('Enter power consumption for each hour: ')))

e = energy_power_consumption(time_data, power_data)



