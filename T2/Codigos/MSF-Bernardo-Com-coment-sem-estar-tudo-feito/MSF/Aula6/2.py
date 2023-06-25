


import matplotlib.pyplot as plt
import numpy as np

dt = 0.001  #sempre igual
massa = 0.45 #ver
r = 0.11 #ver  (raio)
area = np.pi*r**2 
PAr = 1.225 #kg/m^3 #sempre igual
vt = 27.7778 #m/s v = 100/3.6
g = -9.8   #mudar isto leva a                                   **********************************
omega = 400  #ver /Wy
Wz = 0 #ver
Wx = 0 #ver

t = np.arange(0,0.5+dt, dt)
x = np.zeros(t.size)
vx = np.zeros(t.size)
ax = np.zeros(t.size)
ay = np.zeros(t.size)
az = np.zeros(t.size)
y = np.zeros(t.size)
vy = np.zeros(t.size)
z = np.zeros(t.size)
vz = np.zeros(t.size)



z[0] = 23.8
vx[0] = 25.5
vy[0] = 5
vz[0] = -50



for i in range(0,t.size-1):
    t[i+1]=t[i]+dt
    vv=np.sqrt(vx[i]**2+vy[i]**2+vz[i]**2)         # norma de v
    dres=g/vt**2                                   # g = -g *************************************+
    mag=0.5*1.225*0.11*np.pi*0.11**2               # mag = 1/2 * A * PAr * r * w * v    ## w * v = (wy * vz,0,-wy * vx)  ## A = np.pi*(r**2)
    amx=mag*omega*vz[i]/massa
    amz=-mag*omega*vx[i]/massa                      
    ax[i]=-dres*vv*vx[i]+amx
    ay[i]=-g-dres*vv*vy[i]                         # -g = g ******************************************
    az[i]=-dres*vv*vz[i]+amz
    vx[i+1]=vx[i]+ax[i]*dt
    vy[i+1]=vy[i]+ay[i]*dt
    vz[i+1]=vz[i]+az[i]*dt
    x[i+1]=x[i]+vx[i]*dt
    y[i+1]=y[i]+vy[i]*dt
    z[i+1]=z[i]+vz[i]*dt
    
plt.plot(t,x,label="x")
plt.plot(t,y,label="y")
plt.plot(t,z,label="z")
plt.legend()

        