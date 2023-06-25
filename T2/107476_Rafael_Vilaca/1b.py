
import matplotlib.pyplot as plt
import numpy as np

dt = 0.01
n = int(1/dt)
m = 0.45
r = 0.11
area = np.pi*r**2
PAr = 1.225 #kg/m^3
Terminalvelocity = 100*1000/3600 #m/s
t = np.arange(0,1.5+dt, dt)
g = 9.8
Rx = np.zeros(t.size)
Vx = np.zeros(t.size)

Ry = np.zeros(t.size)
Vy = np.zeros(t.size)
Wz = -10

Rz = np.zeros(t.size)
Vz = np.zeros(t.size)


Rz[0] = 23.8
Vx[0] = 25
Vy[0] = 5
Vz[0] = -50

D = g/(Terminalvelocity**2)
mag = 0.5*1.225*0.11*np.pi*0.11**2


for i in range(0,t.size-1):
    vv=np.sqrt(Vx[i]**2+Vy[i]**2+Vz[i]**2)
    
    
    amx = mag * Wz*Vy[i]/m
    amy = -mag * Wz*Vx[i]/m
    
    ax = -D*vv*Vx[i]+amx
    ay = -g-D*vv*Vy[i]+ amy
    az = -D*vv*Vz[i]
    
    Vx[i+1] = Vx[i]+ax*dt
    Vy[i+1] = Vy[i]+ay*dt
    Vz[i+1] = Vz[i]+az*dt
    
    Rx[i+1] = Rx[i] + Vx[i] * dt
    Ry[i+1] = Ry[i] + Vy[i] * dt
    Rz[i+1] = Rz[i] + Vz[i] * dt

for i in range(t.size-1):
    if((Rx[i]) > (20-dt) and (Rx[i-1]) < (20+dt)):            
        print("y_1 -> ",Ry[i])      
        print("y_2 -> ",Ry[i+1])                ## nao funciona logo por observaçao dos graficos é golo
        print("z_1 -> ",Rz[i])      
        print("z_2 -> ",Rz[i+1])
    
plt.plot(t,Rx,label="x")
plt.plot(t,Ry,label="y")
plt.plot(t,Rz,label="z")
plt.legend()
plt.grid()
plt.show()






