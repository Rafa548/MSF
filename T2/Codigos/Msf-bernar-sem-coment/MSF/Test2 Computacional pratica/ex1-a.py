# -*- coding: utf-8 -*-
"""
Created on Sun May 29 20:58:15 2022

@author: draki

Uma bola de ténis é batida junto ao solo (posição inicial 𝑦 = 0) com a velocidade 140 km/h, a fazer um
ângulo de 7º com a horizontal e no sentido positivo dum eixo horizontal OX, sendo OY eixo vertical.
Considerando sempre a resistência do ar,

a) Calcule a trajetória da bola. Qual o alcance?
A velocidade terminal da bola de ténis é 100 km/h.
A bola de ténis tem a massa 57 g.
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.001 # escolher
g = 9.8 
m = 57/1000 # enunciado
v0 = 140/3.6 # enunciado
ang0 = 7/180*np.pi  # enunciado
t = np.arange(0,15+dt, dt) # escolher
TerminalVel = 100/3.6 # enunciado

y0 = 0 # enunciado
x0 = 0 # enunciado

vx0 = v0*np.cos(ang0)
vy0 = v0*np.sin(ang0)

 

x = np.zeros(t.size)
y = np.zeros(t.size)
vx = np.zeros(t.size)
vy = np.zeros(t.size)
v = np.zeros(t.size)
x[0], y[0] = x0, y0
v[0], vx[0], vy[0] = v0, vx0, vy0

D = g/TerminalVel**2

for i in range(t.size-1):
    vAbs = np.sqrt(vx[i]**2+vy[i]**2)
    ax = -D*vx[i]*v[i]
    ay = -D*vy[i]*v[i]

    ay = ay - g
    
    vx[i+1] = vx[i] + ax*dt
    vy[i+1] = vy[i] + ay*dt
    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    v[i+1] = np.linalg.norm((vx[i+1], vy[i+1]))
    if y[i+1] < 0:
        break;
        
    
t = t[:i+2]
x = x[:i+2]
y = y[:i+2]
vx = vx[:i+2]
vy = vy[:i+2]
v = v[:i+2]

plt.plot(x,y)
print("Last x ->", x[-1])