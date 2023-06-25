# -*- coding: utf-8 -*-

from maxminv import maxminv
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

dt = 0.001
m = 1
xeq = 0
g = 9.8

k = 1
b = 0.05
a = 0.002
F0 = 7.5
VForc = 1

t = np.arange(0,300+dt,dt)

x = np.zeros(t.size)
v = np.zeros(t.size)
x[0] = 3
v[0] = 0
for i in range(t.size-1):
    Fx = -k*x[i]*(1+2*a*(x[i]**2))
        
    Fforc = F0*np.cos(VForc*t[i])
    
    Famort = -b*v[i]
    
    ax = (Fx+Fforc+Famort)/m
    
    v[i+1] = v[i] + ax*dt
    x[i+1] = x[i] + v[i+1]*dt
    
plt.plot(t,x)
plt.grid()


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
