# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 17:16:54 2022

@author: draki
"""
import matplotlib.pyplot as plt
import numpy as np


dt = 0.001

t = np.arange(0, 20+dt,dt)
k = 1
m = 1
omega = np.sqrt(k/m)
EM = np.zeros(t.size)
xeq = 1.5
v = np.zeros(t.size)
x = np.zeros(t.size)

f = np.zeros(t.size)
EP = np.zeros(t.size)
v[0] = 0
x[0] = np.sqrt(xeq**2+np.sqrt(1.5/k))

for i in range(t.size-1):
    f[i] = -2*k*(x[i]**2-xeq**2)*x[i]
    a = f[i]/m
    v[i+1] = v[i] + a*dt
    x[i+1] = x[i] + v[i+1]*dt

plt.plot(t,x)
plt.show()