import numpy as np
import matplotlib.pyplot as plt
import math as m
from src.PowerCon import energy_power_consumption

t = int(input('Time(hours): '))
time_data = np.arange(0, t)  
power_data = []
for i in range(t):
    power_data.append(int(input('Enter power consumption for each hour: ')))
e = energy_power_consumption(time_data, power_data)

print('-=Summary=-')
print('Time data: ',t,'hour(s) in total.')
print('Power data: ',power_data,'in Watts.')
print('Energy data: ',e,'in kilo Watts per hour.')

