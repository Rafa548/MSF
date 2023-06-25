#teorica

import matplotlib.pyplot as plt
import numpy as np
dt = 0.01
SolX = 0
SolY = 0

t = np.arange(0,10+dt, dt)

Rx = np.zeros(t.size)
Ry = np.zeros(t.size)

Vx = np.zeros(t.size)
Vy = np.zeros(t.size)

Ax = np.zeros(t.size)
Ay = np.zeros(t.size)

m = 1 # massa solar = massa do sol, neste caso nas equaçoes a massa da terra é anulada logo nao temos que a declarar
      # declaramos apenas a massa do sol = 1.


Rx[0] = 1 # posiçoes iniciais
Ry[0] = 0

Vx[0] = 0 # velocidades iniciais
Vy[0] = 2 * np.pi

g = 4*np.pi**2 # utilizar a constante de gravitaçao no sistema astronomico https://imgur.com/a/IsKjp5d

for i in range(0, t.size-1):
    rr = np.sqrt(Rx[i]**2 + Ry[i]**2)
    Ax[i] = -g*m/rr**3*Rx[i]
    Ay[i] = -g*m/rr**3*Ry[i]
    Vx[i+1] = Vx[i] + Ax[i]*dt
    Vy[i+1] = Vy[i] + Ay[i]*dt
    Rx[i+1] = Rx[i] + Vx[i]*dt
    Ry[i+1] = Ry[i] + Vy[i]*dt

plt.plot(SolX, SolY,"x")
plt.plot(Rx,Ry, label="Euler") # dilata a circunferencia devido ao erro criando um espiral crescente

for i in range(0, t.size-1):
    rr = np.sqrt(Rx[i]**2 + Ry[i]**2)
    Ax[i] = -g*m/rr**3*Rx[i]
    Ay[i] = -g*m/rr**3*Ry[i]
    Vx[i+1] = Vx[i] + Ax[i]*dt
    Vy[i+1] = Vy[i] + Ay[i]*dt
    Rx[i+1] = Rx[i] + Vx[i+1]*dt
    Ry[i+1] = Ry[i] + Vy[i+1]*dt
    
plt.plot(Rx,Ry, label="Euler-Cromer")
plt.show()
plt.legend()