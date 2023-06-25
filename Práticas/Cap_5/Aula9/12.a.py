import numpy as np
import matplotlib.pyplot as plt
import math

t0 = 0
tf = 100
dt = 0.001
n = int((tf-t0)/dt)

m = 75 #kg
u = 0.004 
Cres = 0.9 
A = 0.3 #m^2
v = 1 #m/s
ro = 1.225 #kg/m^3
g = 9.8
cv = 0.4 # 1cv = 735.4975 w
P = cv * 735.4975
x0 = 0
v0 = 1
tolerancia = 0.000001

T = np.linspace(t0,tf,n)
ax = np.empty(T.size)
vx = np.empty(T.size)
x = np.empty(T.size)
v = np.empty(T.size)

vx[0] = v0
x[0] = x0

for i in range(n-1):
    v[i] = math.sqrt(vx[i]**2)
    ax[i] = - u * g - Cres/(2*m)*A*ro*v[i]*vx[i] + P/(m*v[i])
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + v[i]*dt
    if vx[i]-vx[i-1] < tolerancia :
        print(vx[i])
        break
        



v[n-1] = math.sqrt(vx[n-1]**2)
plt.xlabel('T (s)')
plt.ylabel('X (m)')
plt.plot(T, v)
plt.show()