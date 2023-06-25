import numpy as np
import matplotlib.pyplot as plt


m = 75 #kg
u = 0.004 
Cres = 0.9 
A = 0.3 #m^2
v = 30/3.6 #m/s
vx = v
ró = 1.225 #kg/m^3
g = 9.8

P = u * m * g * v + Cres/2*A*ró*v**2*vx

print(P)