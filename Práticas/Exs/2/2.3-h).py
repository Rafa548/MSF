import numpy as np
import matplotlib.pyplot as plt

g = -9.8
v0 = 0
x0 = 0
tf = 3
t0 = 0

xt = 1/2*-9.8*4
dt_1= [0.1,0.01,0.001]
desvio = np.empty(len(dt_1))

for i in (dt_1):
    dt = i
    n = int((tf-t0)/dt)
    t = np.linspace(t0,tf,n)
    v = np.empty(n) #n tem de ser igual ao do linespace
    x = np.empty(n) 
    v[0] = v0   #nao esquecer
    x[0] = x0
    desvio[0] = 0
    for k in range(n-1): # n-1 porque o empty é n, se empty fosse n+1 valor de range era n
        v[k+1] = v[k]+g*dt  # g = acelaraçao logo constante caso contrário seria a[i]
        x[k+1] = x[k]+v[k]*dt # posiçao    

    for k in range(n-1):
        if((t[k]) > (2-dt) and (t[k+1]) < (2+dt)):   #(verificar os pontos onde o tempo está mais perto do 2) // (para instante diferente trocar o 2)
            desvio[k+1] = xt - x[k]
            

plt.plot(dt,desvio)
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.show()
