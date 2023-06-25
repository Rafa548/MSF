from cProfile import label
from maxminv import maxminv, abfourier
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

dt = 0.01
m = 1
xeq = 0
g = 9.8

k = 1
b = 0.05
a = 0.002
F0 = 7.5
VForc = 1

t = np.arange(0,600+dt,dt)

x = np.zeros(t.size)
v = np.zeros(t.size)
x[0] = 3
v[0] = 0

for i in range(t.size-1):
    Fx = -k*x[i]*(1+2*a*(x[i]**2))
        
    Fforc = F0*np.cos(VForc*t[i])
    
    Famort = -b*v[i]
    
    ax = (Fx+Fforc+Famort)/m
    
    v[i+1] = v[i] + ax*dt
    x[i+1] = x[i] + v[i+1]*dt

ind_peaks = find_peaks(x)[0]
n = np.arange(0,11,1)
af = np.zeros(n.size)
bf = np.zeros(n.size)
tmax = np.zeros(ind_peaks.size)
angmax = np.zeros(ind_peaks.size)
plt.plot(t[59000:60000],x[59000:60000], label="original")


for i in range(tmax.size):
    k = ind_peaks[i]
    tmax[i], angmax[i] = maxminv(t[k-1],t[k],t[k+1],x[k-1],x[k],x[k+1])
    
Ang_Num = angmax[-1]
T_Num = (tmax[-1]-tmax[-2])
print("\nA amplitdue é {:0.5f}º".format(Ang_Num))
print("\nO periodo é {:0.5f}s".format(T_Num))
for i in range(n.size):
    af[i],bf[i] = abfourier(t, x, ind_peaks[-2], ind_peaks[-1], i)

print("\n{:^15}{:^15}{:^15}{:^15}".format("n","an","bn","sqrt(an^2+bn^2)"))

omega = 6.28319
for i in range(n.size):
    plt.plot(t[59000:60000], af[i]*np.cos(2*np.pi/omega*i*t[59000:60000])+bf[i]*np.sin(2*np.pi/omega*i*t[59000:60000]), label=n[i])
    print("{:^15}{:^15.5f}{:^15.5f}{:^15.5f}".format(n[i],af[i],bf[i],np.sqrt(af[i]**2+bf[i]**2)))

plt.legend()
plt.show()