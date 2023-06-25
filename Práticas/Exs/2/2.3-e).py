import numpy as np
import matplotlib.pyplot as plt

g = -9.8
v0 = 0
x0 = 0
tf = 3
t0 = 0

dt= 0.001
n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)
v = np.empty(n) #n tem de ser igual ao do linespace
x = np.empty(n) 
v[0] = v0   #nao esquecer
x[0] = x0
for i in range(n-1): # n-1 porque o empty é n, se empty fosse n+1 valor de range era n
    v[i+1] = v[i]+g*dt  # g = acelaraçao logo constante caso contrário seria a[i]
    x[i+1] = x[i]+v[i]*dt # posiçao    

for i in range(n-1):
    if((t[i]) > (2-dt) and (t[i+1]) < (2+dt)):   #(verificar os pontos onde o tempo está mais perto do 2) // (para instante diferente trocar o 2)
        print("dt, t, vy = ",dt,t[i],x[i])      
        print("dt, t, vy = ",dt,t[i+1],x[i+1])
plt.plot(t,x)
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.show()