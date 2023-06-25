
import matplotlib.pyplot as plt
import numpy as np

dt = 0.01

k = 1
m = 1
Fz = 7.5
b = 0.05
wf = 1 #rad

w = np.sqrt(k/m)

t = np.arange(0, 400+dt, dt)

x = np.zeros(t.size)
v = np.zeros(t.size)
a = np.zeros(t.size)
x[0] = 4
v[0] = 0

for i in range(t.size-1):
    a[i] = (-k/m)*x[i]-(b*v[i])/m + Fz*np.cos(wf *t[i])/m 
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i]+v[i+1]*dt
    
    
plt.plot(t,x)
plt.show()
