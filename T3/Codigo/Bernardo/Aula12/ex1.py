# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 16:11:02 2022

@author: draki
"""

from maxminv import maxminv
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks


ang0 = [1,5,10,15,20,30]
dt = 0.0001 

for angle in ang0:
    
    t = np.arange(0, 25+dt,dt)
    g = 9.8
    l = 1.0

    ang = np.zeros(t.size)
    w = np.zeros(t.size)

    ang[0] = angle/180*np.pi
    w[0] = 0

    for i in range(t.size-1):
        alfa = -g/l*np.sin(ang[i])
        w[i+1] = w[i] + alfa*dt
        ang[i+1] = ang[i] + w[i+1]*dt
        
    plt.plot(t,ang)
    ind_peaks = find_peaks(ang)[0]
    tmax = np.zeros(ind_peaks.size)
    angmax = np.zeros(ind_peaks.size)

    for i in range(tmax.size):
        k = ind_peaks[i]
        tmax[i], angmax[i] = maxminv(t[k-1],t[k],t[k+1],ang[k-1],ang[k],ang[k+1])
    
    Ang_Num = np.mean(angmax)/np.pi*180

    T_Num = (tmax[-1]-tmax[-2])
    print("\n\nPara o Angulo inicial {}".format(angle))
    print("\nA amplitdue é {:0.5f}º".format(Ang_Num))
    print("\nO periodo é {:0.5f}s".format(T_Num))
