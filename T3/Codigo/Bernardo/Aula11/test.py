# -*- co+ding: utf-8 -*-
"""
Created on Tue Jun  7 15:17:36 2022

@author: draki
"""
import matplotlib.pyplot as plt
import numpy as np

def rk4(t,vx,acelera,dt):
    """
    Integração numérica de equação diferencial de 2ª ordem:
			dvx/dt = ax(t,vx)    de valor inicial
	Erro global:  proporcional a dt**4
    acelera=dvx/dt=Força(t,vx)/massa     : acelera é uma FUNÇÃO
    input:  t = instante de tempo
            vx(t) = velocidade
            dt = passo temporal 
    output: vxp = vx(t+dt)
    """
    ax1=acelera(t,vx)
    c1v=ax1*dt
    ax2=acelera(t+dt/2.,vx+c1v/2.)
    c2v=ax2*dt       			# predicto:  vx(t+dt) * dt
    ax3=acelera(t+dt/2.,vx+c2v/2.)
    c3v=ax3*dt
    ax4=acelera(t+dt,vx+c3v)
    c4v=ax4*dt
          
    vxp=vx+(c1v+2.*c2v+2.*c3v+c4v)/6.
    return vxp

def acelera(t,vx):
    ax=g-g/vt**2*np.abs(vx)*vx
    return ax

global g,vt
g = 9.8
vt = 6.8

dt = 0.1
t = np.arange(0,2+dt,dt)
Vx = np.zeros(t.size)
X = np.zeros(t.size)
Ax = np.zeros(t.size)



for i in range(t.size-1):
    Vx[i+1] = rk4(t[i], Vx[i], acelera, dt)
    X[i+1] = X[i] + Vx[i]*dt

plt.plot(t,Vx)
print(Vx[-1])