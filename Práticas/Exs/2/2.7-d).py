import matplotlib.pyplot as plt
import numpy as np

vi = 10 # m/s
dt = 0.001
g = 9.8
t0 = 0
tf = 2.3
n = int((tf-t0)/dt)

T = np.linspace(0,2.3,n)
v = np.empty(T.size)
y = np.empty(T.size)
a = np.empty(T.size)

v[0] = 10
a[0] = 0
D = g/(27.7778**2) # D= g/vt**2

for i in range(n-1):
        a[i] = D * v[i] * np.abs(v[i]) - g
        v[i+1] = v[i] + a[i] * dt # velocidade no instante
        y[i+1] = y[i] + v[i] * dt # posiçao no instante

for i in range(n-1):
    if((v[i]) > (0-dt) and (v[i+1]) < (0+dt)):      #(verificar os pontos onde a velocidade está mais perto do 0) // (para v diferente trocar o 0)
        print("dt, t, vy, y = ",dt,T[i],v[i],y[i])      
        print("dt, t, vy, y = ",dt,T[i+1],v[i+1],y[i+1])

for i in range(n-1):
    if((y[i]) > (0-dt) and (y[i+1]) < (0+dt)):      #(verificar os pontos onde a posiçao está mais perto do 0) // (para pos diferente trocar o 0)
        print("dt, t, vy, y = ",dt,T[i],v[i],y[i])       
        print("dt, t, vy, y = ",dt,T[i+1],v[i+1],y[i+1])

plt.xlabel('Tempo (s)')
plt.ylabel('X (m)')
plt.plot(T, y, label="pos")
plt.legend()
plt.show()