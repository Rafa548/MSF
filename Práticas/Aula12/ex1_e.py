
import matplotlib.pyplot as plt
import numpy as np

dt = 0.001

k = 1
m = 1
Fz = 7.5
b = 0.05
wf = 1 #rad
w = np.sqrt(k/m)
xeq=0

t = np.arange(0, 400+dt, dt)

arrayx = []
tempos = []
periodo = []
x = np.zeros(t.size)
v = np.zeros(t.size)
a = np.zeros(t.size)
x[0] = -2
v[0] = -4
Em = np.zeros(t.size)

for i in range(t.size-1):
    a[i] = (-k/m)*x[i]-(b*v[i])/m + Fz*np.cos(wf *t[i])/m 
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i]+v[i+1]*dt
    Em[i] = m*(0.5*v[i]**2 + 0.5*(k*x[i]**2-xeq**2))

Em[t.size-1] = m*(0.5*v[t.size-1]**2 + 0.5*(k*x[t.size-1]**2-xeq**2))


for i in range(t.size-1):
    if (x[i-1]<x[i]>x[i+1] and i>0 and t[i]>250):   #mudar 250 para o estacionário que se vê no grafico
        arrayx.append(x[i])
        tempos.append(t[i])

for i in range(0,len(tempos)-1):
    periodo.append(tempos[i+1]-tempos[i])           


#print("Periodo ->",np.mean(periodo))
#print("Amplitude ->" ,np.mean(arrayx))

#plt.plot(t,x)
#plt.show()

plt.plot(t,Em)
plt.show()
