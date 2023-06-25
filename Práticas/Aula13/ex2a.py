
import matplotlib.pyplot as plt
import numpy as np

dt = 0.01

k = 1
m = 1
Fz = 7.5
b = 0.05
wf = 1 #rad
w = np.sqrt(k/m)
alpha = 0.002

t = np.arange(0, 400+dt, dt)

arrayx = []
tempos = []
periodo = []
x = np.zeros(t.size)
v = np.zeros(t.size)
a = np.zeros(t.size)
x[0] = 4
v[0] = 0

for i in range(t.size-1):
    a[i] = (-k/m)*x[i]*(1+2*alpha*x[i]**2)-(b*v[i])/m + Fz*np.cos(wf *t[i])/m 
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i]+v[i+1]*dt
    


for i in range(t.size-1):
    if (x[i-1]<x[i]>x[i+1] and i>0 and t[i]>200):
        arrayx.append(x[i])
        tempos.append(t[i])

for i in range(0,len(tempos)-1):
    periodo.append(tempos[i+1]-tempos[i])           


print("Periodo ->",np.mean(periodo))
print("Amplitude ->" ,np.mean(arrayx))

plt.plot(t,x)
plt.show()
