import numpy as np
import matplotlib.pyplot as plt

g = -9.8
v0 = 0
tf = 4
t0 = 0

dt= 0.001
n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)
v = np.empty(n) #n tem de ser igual ao do linespace
v[0] = v0   #nao esquecer
for i in range(n-1): # n-1 porque o empty é n, se empty fosse n+1 valor de range era n
    v[i+1] = v[i]+g*dt

for i in range(n-1):
    if((t[i]) > (3-dt) and (t[i+1]) < (3+dt)):   #(verificar os pontos onde o tempo está mais perto do 3) // (para instante diferente trocar o 3)
        print("dt, t, vy = ",dt,t[i],v[i])      
        print("dt, t, vy = ",dt,t[i+1],v[i+1])


plt.plot(t,v)
plt.xlabel("t (s)")
plt.ylabel("v (m/s)")
plt.show()



