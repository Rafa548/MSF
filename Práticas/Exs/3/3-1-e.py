import matplotlib.pyplot as plt
import numpy as np

v0 = 100 * 1000/3600
dt = 0.001
g = 9.8
t0 = 0
tf = 1
vt = 100/3.6
x0 = 0
y0 = 0
ang = np.radians(10)
n = int((tf-t0)/dt)
v0x = v0 * np.cos(ang)
v0y = v0 * np.sin(ang)

T = np.linspace(t0,tf,n)
ax = np.empty(T.size)
ay = np.empty(T.size)
vx = np.empty(T.size)
vy = np.empty(T.size)
y = np.empty(T.size)
x = np.empty(T.size)
v = np.empty(T.size)

x[0] = x0
y[0] = y0
D = g/vt**2
vx[0] = v0 * np.cos(ang)
vy[0] = v0 * np.sin(ang)

for i in range(n-1):
        v[i] = np.sqrt(vy[i]**2+vx[i]**2)
        ay[i] = -D*vy[i]*v[i]-g
        ax[i] = -D*vx[i]*v[i]
        vx[i+1] = vx[i] + ax[i] * dt
        vy[i+1] = vy[i] + ay[i] * dt 
        y[i+1] = y[i] + vy[i] * dt
        x[i+1] = x[i] + vx[i] * dt  


xan = v0x * T + x0
yan = v0y * T - (0.5*g*T**2) + y0

plt.xlabel('Y (m)')
plt.ylabel('X (m)')
plt.plot(x, y)
plt.plot(xan, yan)
plt.show()