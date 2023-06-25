import numpy as np
import matplotlib.pyplot as plt




def acelera(t,x,vx):
    ax = g-g/vT**2*np.abs(vx)*vx
    return ax





def rk4(t,x,vx,dt):
    """
    Integração numérica de equação diferencial de 2ª ordem:
			d2x/dt2 = ax(t,x,vx)    com dx/dt= vx    de valor inicial
	Erro global:  proporcional a dt**4
    acelera=dvx/dt=Força(t,x,vx)/massa      : acelera é uma FUNÇÃO
    input:  t = instante de tempo
            x(t) = posição
            vx(t) = velocidade
            dt = passo temporal 
    output: xp = x(t+dt)
		    vxp = vx(t+dt)
    """
    ax1=acelera(t,x,vx)
    c1v=ax1*dt
    c1x=vx*dt
    ax2=acelera(t+dt/2.,x+c1x/2.,vx+c1v/2.)
    c2v=ax2*dt
    c2x=(vx+c1v/2.)*dt			# predicto:  vx(t+dt) * dt
    ax3=acelera(t+dt/2.,x+c2x/2.,vx+c2v/2.)
    c3v=ax3*dt
    c3x=(vx+c2v/2.)*dt
    ax4=acelera(t+dt,x+c3x,vx+c3v)
    c4v=ax4*dt
    c4x=(vx+c3v)*dt
      
    xp=x+(c1x+2.*c2x+2.*c3x+c4x)/6.
    vxp=vx+(c1v+2.*c2v+2.*c3v+c4v)/6.
    return xp,vxp

tf = 5
ti = 0
dt = 0.001
n = (tf-ti)/dt
n1 = int (n)

t = np.linspace(ti,tf,n1)
vx = np.empty(n1)
x = np.empty(n1)
xrk4 = np.empty(n1)
vxrk4 = np.empty(n1)
g = 9.8
vT = 6.8
x0 = 0
vx0 = 0
t[0] = 0
x[0] = x0
vx[0] = vx0
vxrk4[0] = vx0
xrk4[0] = x0


for i in range(n1-1):
    #rk4
    xrk4[i+1],vxrk4[i+1] = rk4(t[i],xrk4[i],vxrk4[i],dt)

plt.plot(t,vxrk4)
plt.show()

