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

a) Faça o diagrama de energia desta energia potencial. Qual o movimento quando a energia total for menor
que 2 J?
"""

import matplotlib.pyplot as plt
import numpy as np
k = 1.2
a = -0.01
m = 1500
x = np.arange(-100,100, 1) 
f = -k*x - 3*a*x**2
Ep = 0.5*k*x**2+a*x**3

plt.plot(x,Ep)