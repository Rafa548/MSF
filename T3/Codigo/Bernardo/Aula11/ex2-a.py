# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 17:22:45 2022

@author: draki
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-6,6.0001,0.0001)

EP = 0.5*1*(x**2-1.5**2)**2
plt.ylim([0,10])
plt.plot(x, EP)
plt.plot([-6,6],[1,1])
