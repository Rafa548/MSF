# -*- coding: utf-8 -*-
"""
Created on Sun May 29 20:58:15 2022

@author: draki

Uma bola de ténis é batida junto ao solo (posição inicial 𝑦 = 0) com a velocidade 140 km/h, a fazer um
ângulo de 7º com a horizontal e no sentido positivo dum eixo horizontal OX, sendo OY eixo vertical.
Considerando sempre a resistência do ar,

b) Calcule o trabalho efetuado pela força de resistência do ar desde que o jogador bateu a bola e esta atingiu
o solo.
Use a aproximação trapezoidal para calcular os integrais.

A velocidade terminal da bola de ténis é 100 km/h.
A bola de ténis tem a massa 57 g.
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
g = 9.8
m = 57/1000
v0 = 140/3.6
ang0 = 7/180*np.pi
t = np.arange(0,15+dt, dt)
TerminalVel = 100*1000/3600

y0 = 0
x0 = 0
vx0 = v0*np.cos(ang0)
vy0 = v0*np.sin(ang0)

E0 = m*(0.5*v0**2 + g*y0) # equaçao
 
x = np.zeros(t.size)
y = np.zeros(t.size)
vx = np.zeros(t.size)
vy = np.zeros(t.size)
v = np.zeros(t.size)
x[0], y[0] = x0, y0
v[0], vx[0], vy[0] = v0, vx0, vy0

D = g/TerminalVel**2
f = np.zeros(t.size)

Wres = np.zeros(t.size)

for i in range(t.size-1):
    vAbs = np.sqrt(vx[i]**2+vy[i]**2)
    ax = -D*vx[i]*v[i]
    ay = -D*vy[i]*v[i]
    f[i] = m*(ax*vx[i]+ay*vy[i])
    ay = ay - g
    
    vx[i+1] = vx[i] + ax*dt
    vy[i+1] = vy[i] + ay*dt
    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    v[i+1] = np.linalg.norm((vx[i+1], vy[i+1]))
    if y[i+1] <= 0:
        break;
        

    

t = t[:i+2]
x = x[:i+2]
y = y[:i+2]
vx = vx[:i+2]
vy = vy[:i+2]
v = v[:i+2]
f = f[:i+2]
Wres = Wres[:i+2]

for i in range(1,t.size):
    Wres[i] = (0.5*(f[0]+f[i])+np.sum(f[1:i]))*dt # metodo trapezoidal (trabalho da força em todos os instantes)

fig1, ax = plt.subplots(1, 2, figsize=(13,6), layout="constrained")
EM = m*(0.5*v**2 + g*y)

ax[0].plot(x, y)

ax[1].plot(t, EM, t, Wres, t, EM-Wres) #EM ; Wres; EM With no Res

plt.show()

Wres1 = (0.5*(f[0]+f[-1])+np.sum(f[1:-1]))*dt #

print(EM[0])
print(EM[-1])
print(Wres1)
print(E0 + Wres1)
