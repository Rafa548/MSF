# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 19:22:04 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

v0 = 100/3.6  # m/s
teta = np.radians(16)
dt = 0.001
g = 9.8
t0 = 0
tf = 2

vt = 100/3.6  # m/s

n = int((tf-t0)/dt)
t = np.linspace(t0, tf, n)

vx = np.empty(n)
vy = np.empty(n)
vz = np.empty(n)

ax = np.empty(n)
ay = np.empty(n)
az = np.empty(n)

x = np.empty(n)
y = np.empty(n)
z = np.empty(n)

x[0] = 0
y[0] = 0
z[0] = 0

vx[0] = v0*np.cos(teta)
vy[0] = v0*np.sin(teta)
vz[0] = 0

d = g/vt**2

for i in range(n-1):

    ay[i] = -d*abs(vx[i])*vy[i]-g
    ax[i] = -d*vx[i]*abs(vx[i])
    az[i] = 0

    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt
    vz[i+1] = vz[i] + az[i]*dt

    y[i+1] = y[i] + vy[i] * dt
    x[i+1] = x[i] + vx[i] * dt
    z[i+1] = z[i] + vz[i] * dt
    if x[i+1] > 20:
        break



for i in range(n-1):
    if (x[i+1] >=20):
        print("A altura no x=20m é {:0.2f} m".format(y[i]))
        plt.plot(x[i], y[i], "o", label="x = 20")
        break
for i in range(n-1):
    if (y[i+1] < y[i]):
        print("A altura max é {:0.2f} m".format(y[i+1]))
        plt.plot(x[i+1], y[i+1], "o", label="Altura máxima")
        break
for i in range(n-1):
    if (y[i+1]*y[i] < 0):
        print("Alcance {:0.2f} m".format(x[i+1]))
        plt.plot(x[i+1], y[i+1], "o", label="Alcance")
        break

plt.plot(x, y)
plt.legend()
plt.show()
