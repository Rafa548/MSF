# -*- coding: utf-8 -*-
"""
Created on Mon May 30 11:12:39 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
g = 9.8
m = 57/1000
v0 = 100/3.6
ang0 = 7/180*np.pi
t = np.arange(0,15+dt, dt)
TerminalVel = 100*1000/3600

y0 = 0
x0 = 0
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