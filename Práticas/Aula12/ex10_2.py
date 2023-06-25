
import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
g = 9.8
t = np.arange(0, 50+dt, dt)
L=1

tempos = []
periodo = []
teta = np.zeros(t.size)
w = np.zeros(t.size)
a = np.zeros(t.size)
w[0] = 0    #velocidade angular
teta[0] = np.radians(1)  #angulo rad



for i in range(t.size-1):
    a[i] = (-g/L * np.sin(teta[i]))
    w[i+1] = w[i] + a[i]*dt
    teta[i+1] = teta[i]+w[i+1]*dt

for i in range(t.size-1):
    if (teta[i-1]<teta[i]>teta[i+1] and i>0):
        tempos.append(t[i])

for i in range(0,len(tempos)-1):
    periodo.append(tempos[i+1]-tempos[i]) 

print("Periodo ->",np.mean(periodo))              

#plt.plot(t,np.degrees(teta))
#plt.show()