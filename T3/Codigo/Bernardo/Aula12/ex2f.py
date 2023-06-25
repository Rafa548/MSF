# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:22:03 2022

@author: draki
"""

from maxminv import maxminv, abfourier
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
    


ind_peaks = find_peaks(x)[0]
n = np.arange(0,11,1)
Aaf = np.zeros(n.size)
Abf = np.zeros(n.size)
tmax = np.zeros(ind_peaks.size)
angmax = np.zeros(ind_peaks.size)

for i in range(tmax.size):
    k = ind_peaks[i]
    tmax[i], angmax[i] = maxminv(t[k-1],t[k],t[k+1],x[k-1],x[k],x[k+1])
    
Ang_Num = angmax[-1]

T_Num = (tmax[-1]-tmax[-2])
print("\nA amplitdue é {:0.5f}º".format(Ang_Num))
print("\nO periodo é {:0.5f}s".format(T_Num))
for i in range(n.size):
    Aaf[i],Abf[i] = abfourier(t, x, ind_peaks[-2], ind_peaks[-1], i)

fig1, ax = plt.subplots(2, 2, figsize=(13,6), layout="constrained")
ax[0][0].bar(n,Aaf,width=0.1, edgecolor="white", linewidth=0.7)
ax[0][1].bar(n,Abf,width=0.1, edgecolor="white", linewidth=0.7)
print("A)\n{:^15}{:^15}{:^15}{:^15}".format("n","an","bn","sqrt(an^2+bn^2)"))
for i in range(n.size):
    print("{:^15}{:^15.5f}{:^15.5f}{:^15.5f}".format(n[i],Aaf[i],Abf[i],np.sqrt(Aaf[i]**2+Abf[i]**2)))

print("\n\n\n\nC)")
"-----------------------------------------------------------------------------"

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

v[0] = -4
x[0] = -2

for i in range(t.size-1):
    a = (-k*x[i]-b*v[i]+F0*np.cos(Vforca*t[i]))/m
    v[i+1] = v[i] + a*dt
    x[i+1] = x[i] + v[i+1]*dt
    
ind_peaks = find_peaks(x)[0]

n = np.arange(0,11,1)
Caf = np.zeros(n.size)
Cbf = np.zeros(n.size)

for i in range(n.size):
    Caf[i],Cbf[i] = abfourier(t, x, ind_peaks[-2], ind_peaks[-1], i)

fig1, ax = plt.subplots(2, 2, figsize=(13,6), layout="constrained")
ax[1][0].bar(n,Caf,width=0.1, edgecolor="white", linewidth=0.7)
ax[1][1].bar(n,Cbf,width=0.1, edgecolor="white", linewidth=0.7)
print("{:^15}{:^15}{:^15}{:^15}".format("n","an","bn","sqrt(an^2+bn^2)"))
for i in range(n.size):
    print("{:^15}{:^15.5f}{:^15.5f}{:^15.5f}".format(n[i],Caf[i],Cbf[i],np.sqrt(Caf[i]**2+Cbf[i]**2)))