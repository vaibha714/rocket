import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

data = np.loadtxt("data.csv", delimiter = ",")
time = data[:,1]
altitude = data[:,0]

max_height = np.max(altitude)
max_time = time[np.argmax(altitude)]

#VELOCITY CALCULATIONS
delta_x = np.diff(altitude)
delta_time = np.diff(time)
velocity = delta_x/delta_time

b, a = butter(N=4, Wn = 0.1, btype = "low") #Wn is the normalized cutoff frequency, telling scipy the frequency above which to block
filtered = filtfilt(b,a,velocity)


#PLOTTING HEIGHT AND VELOCITY
plt.figure()
plt.subplot(211)
plt.axis((0,2.5,0,8))
plt.ylabel("Height")
plt.plot(time,altitude, "k", max_time, max_height, "go")

plt.subplot(212)
plt.ylabel("Velocity")
plt.xlabel("Time")
plt.plot(time[:-1], velocity, "r", time[:-1], filtered, "k")
plt.show()