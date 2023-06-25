# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:02:45 2022

@author: draki
"""

from maxminv import maxminv
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

dt = 0.001 
t = np.arange(0, 300+dt,dt)
g = 9.8
m = 1
x = np.zeros(t.size)
v = np.zeros(t.size)

Vforca = 1
F0 = 7.5
b = 0.05
k = 1

v[0] = 0
x[0] = 4

for i in range(t.size-1):
    a = (-k*x[i]-b*v[i]+F0*np.cos(Vforca*t[i]))/m
    v[i+1] = v[i] + a*dt
    x[i+1] = x[i] + v[i+1]*dt
    
plt.plot(t,x)   

ind_peaks = find_peaks(x)[0]
tmax = np.zeros(ind_peaks.size)
angmax = np.zeros(ind_peaks.size)

for i in range(tmax.size):
    k = ind_peaks[i]
    tmax[i], angmax[i] = maxminv(t[k-1],t[k],t[k+1],x[k-1],x[k],x[k+1])
    
Ang_Num = angmax[-1]

T_Num = (tmax[-1]-tmax[-2])
print("\nA amplitdue é {:0.5f}º".format(Ang_Num))
print("\nO periodo é {:0.5f}s".format(T_Num))
