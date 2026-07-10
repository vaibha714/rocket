import numpy as np

v0 = 12 #inital velocity of model rocket
g = 9.8
time = np.linspace(0,3,500, endpoint = True)

time_squared = time**2 
height = v0 * time -(.5*g*time_squared)

indices = height > 0
pos = height[indices]
new_time = time[indices]

gaussian_noise = np.random.normal(0,.05,new_time.size)

messy_height = pos + gaussian_noise

result = np.column_stack((messy_height,new_time))
np.savetxt("data.csv", result, delimiter= ",", header = "Messy Height vs Time")


