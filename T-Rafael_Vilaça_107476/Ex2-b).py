import numpy as np
import matplotlib.pyplot as plt

g = 9.8
v0 = 0
x0 = 800
tf = 1
t0 = 0

dt= 0.001
n = int((tf-t0)/dt)
T = np.linspace(t0,tf,n)
v = np.empty(T.size)
y = np.empty(T.size)
a = np.empty(T.size)
floor = np.zeros(n)
D = g/(5**2) 
v[0] = v0   
y[0] = x0

for i in range(n-1): 
    a[i] = D * v[i] * np.abs(v[i]) - g
    v[i+1] = v[i] + a[i] * dt 
    y[i+1] = y[i] + v[i] * dt    

for i in range(n-1):
    if((T[i]) > (10-dt) and (T[i+1]) < (10+dt)):   
        print("dt, t, x = ",dt,T[i],y[i])        
        print("dt, t, x = ",dt,T[i+1],y[i+1])

plt.plot(T,y)
plt.plot(T,floor)
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.show()