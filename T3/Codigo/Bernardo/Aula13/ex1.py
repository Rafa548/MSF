# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def acelera(t,vx):
    ax=g-g/vt**2*np.abs(vx)*vx
    return ax


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

dtarr = [1, 0.1, 0.01, 0.001, 0.0001]

g = 9.8
vt = 6.8
tf = 2

print("\n{:^15}{:^15}{:^15}".format("DT","Euler","RK4"))
for dt in dtarr:
    teuler = np.arange(0,tf+dt,dt)
    
    yeuler = np.zeros(teuler.size)
    vyeuler = np.zeros(teuler.size)
    ayeuler = np.zeros(teuler.size)
    
    trk4 = np.arange(0,tf+dt,dt)
    
    yrk4 = np.zeros(trk4.size)
    vrk4 = np.zeros(trk4.size)
    ark4 = np.zeros(trk4.size)
    
    for i in range(teuler.size-1):
        ayeuler[i] = acelera(teuler[i],vyeuler[i])
        vyeuler[i+1] = vyeuler[i] + ayeuler[i]*dt
        yeuler[i+1] =yeuler[i] + vyeuler[i+1]*dt
        
    for i in range(trk4.size-1):
        vrk4[i+1] = rk4(trk4[i],vrk4[i],acelera,dt)
        yrk4[i+1] = yrk4[i] + vrk4[i]*dt
        
    print("\n{:^15.8f}{:^15.8f}{:^15.8f}".format(dt, vyeuler[-1], vrk4[-1]))