# -*- coding: utf-8 -*-
"""
Created on Sun May 29 20:58:15 2022

@author: draki

Um corpo de massa 1.5 kg move-se num oscilador cúbico. Se a posição de equilíbrio for a origem do eixo
𝑥𝑒𝑞 = 0 m, o oscilador tem a energia potencial:
    
𝐸𝑝 = 1/2 * 𝑘 * x^2 + 𝛼 * 𝑥^3

exerce no corpo a força

𝐹𝑥 = −𝑘 * 𝑥 − 3 * 𝛼 * 𝑥^2

Considere 𝑘 = 1.2 N/m e 𝛼 = − 0.01 N/m2.

b) Calcule a lei do movimento, quando a posição inicial for 3.5 m e a velocidade inicial 2.0 m/s? Quanto é a
energia mecânica? Entre que limites se efetua o movimento e a frequência e o período do movimento?
Apresente os resultados com a precisão de 4 algarismos.
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.0001

k = 1.2
a = -0.01
m = 1.5

w = np.sqrt(1.2/m)
t = np.arange(0, 20+dt, dt)

rx = np.zeros(t.size)
rx[0] = 3.5
vx = np.zeros(t.size)
vx[0] = 2.0
ax = np.zeros(t.size)

for i in range(t.size-1):
    f = -k*rx[i] - 3*a*(rx[i]**2)
    ax[i] = f/m
    vx[i+1] = vx[i] + ax[i]*dt
    rx[i+1] = rx[i] + vx[i+1]*dt

plt.plot(t, rx)
plt.plot(t,vx)

for j in range(t.size-1):
    value = 0.0002
    if abs(vx[j]) < value:
        print(vx[j])
        print(t[j])