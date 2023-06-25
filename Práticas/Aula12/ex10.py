
import matplotlib.pyplot as plt
import numpy as np

dt = 0.01
g = 9.8
L=1
t = np.arange(0, 50+dt, dt)

teta = np.zeros(t.size)
w = np.zeros(t.size)
a = np.zeros(t.size)
w[0] = 0    #velocidade angular
teta[0] = np.radians(1)  #angulo rad



for i in range(t.size-1):
    a[i] = (-g/L * np.sin(teta[i]))
    w[i+1] = w[i] + a[i]*dt
    teta[i+1] = teta[i]+w[i+1]*dt


plt.plot(t,np.degrees(teta))
plt.show()