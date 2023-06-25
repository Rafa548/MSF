
import matplotlib.pyplot as plt
import numpy as np

dt = 0.01

k = 1
m = 1
x_eq = 1.5
Em = 1        ## joule

w = np.sqrt(k/m)

t = np.arange(0, 200+dt, dt)


x = np.zeros(t.size)
v = np.zeros(t.size)
a = np.zeros(t.size)
Ep = np.zeros(t.size)
x[0] = np.sqrt(np.sqrt(2*Em/k) + x_eq**2)
v[0] = 0

for i in range(t.size-1):
    a[i] = (-2*k/m)*(x[i]**2-x_eq**2)*x[i]
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i]+v[i+1]*dt
    Ep[i] = 1/2*k*(x[i]**2-x_eq**2)**2    
    
Ep[i+1] = 1/2*k*(x[i+1]**2-x_eq**2)**2
plt.plot(x,Ep)
plt.show()
