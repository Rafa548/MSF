
import matplotlib.pyplot as plt
import numpy as np

dt = 0.01

k = 1
m = 1
var_t = 0
c = 0


w = np.sqrt(k/m)

t = np.arange(0, 200+dt, dt)

arrayx = []
tempos = []
periodo = []
x = np.zeros(t.size)
v = np.zeros(t.size)
a = np.zeros(t.size)
x[0] = 4
v[0] = 0

for i in range(t.size-1):
    a[i] = (-k/m)*x[i]
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i]+v[i+1]*dt

for i in range(t.size-1):
    if (x[i-1]<x[i]>x[i+1] and i>0):
        arrayx.append(x[i])
        tempos.append(t[i])

##for i in range(1,len(tempos)-1):                  opcional este ou o de baixo
##    periodo.append(tempos[i]-tempos[i-1])

for i in range(0,len(tempos)-1):
    periodo.append(tempos[i+1]-tempos[i])           


print("Periodo ->",np.mean(periodo))



print("Amplitude ->" ,np.mean(arrayx))

#plt.plot(t,x)
#plt.show()
