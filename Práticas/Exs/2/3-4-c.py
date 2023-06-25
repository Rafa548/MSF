import matplotlib.pyplot as plt
import numpy as np

v0 = 130/3.6
dt = 0.001
g = 9.8
t0 = 0
tf = 2
vt = 100/3.6
x0 = (-10)
y0 = 1
z0 = 0
ang = np.radians(10)
n = int((tf-t0)/dt)
v0x = v0 * np.cos(ang)
v0y = v0 * np.sin(ang)
v0z = 0
raio = 0.067/2
area = np.pi*raio**2
omega = -100
P_Ar = 1.225
massa = 0.057
mag = 1/2 * area * P_Ar * raio / massa

T = np.linspace(t0,tf,n)
ax = np.empty(T.size)
ay = np.empty(T.size)
az = np.empty(T.size)
vx = np.empty(T.size)
vy = np.empty(T.size)
vz = np.empty(T.size)
y = np.empty(T.size)
x = np.empty(T.size)
z = np.empty(T.size)
v = np.empty(T.size)

x[0] = x0
y[0] = y0
z[0] = z0
D = g/vt**2
vx[0] = v0 * np.cos(ang)
vy[0] = v0 * np.sin(ang)
vz[0] = 0

for i in range(n-1):
    
        v[i] = np.sqrt(vy[i]**2+vx[i]**2+vz[i]**2)
        amx =- mag*omega*vy[i]
        amy = mag*omega*vx[i]

        ay[i] = -D*vy[i]*v[i]-g + amy
        ax[i] = -D*vx[i]*v[i] + amx
        az[i] = 0
        vx[i+1] = vx[i] + ax[i] * dt
        vy[i+1] = vy[i] + ay[i] * dt
        vz[i+1] = vz[i] + az[i] * dt  
        y[i+1] = y[i] + vy[i] * dt
        x[i+1] = x[i] + vx[i] * dt
        z[i+1] = z[i] + vz[i] * dt  

for i in range(n-1):
    if((vy[i]) > (0-dt) and (vy[i+1]) < (0+dt)):            #vy é importante
        print("A_max_1 -> ",y[i])      
        print("A_max_2 -> ",y[i+1])

for i in range(n-1):
    if(y[i+1]*y[i]<0):                                  # para o alcance melhor opção
        print("Alcance_1 -> ",x[i])
        print("Alcance_2 -> ",x[i+1])



plt.xlabel('Y (m)')
plt.ylabel('X (m)')
plt.plot(x, y)
plt.show()
