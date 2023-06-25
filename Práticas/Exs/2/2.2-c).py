import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

t_1 = np.linspace(0,4,100)
vt_1 = 6.8
g_1 = 9.8

#y = (vt**2/g)*np.log(np.cosh(g*t/vt))

t = sym.Symbol("t")
v = sym.Symbol("v")
vt = sym.Symbol("vt")
g = sym.Symbol("g")
D = sym.Symbol("D")


D = sym.Derivative((vt**2/g)*sym.log(sym.cosh(g*t/vt)),t, evaluate= True)
print("dy/dt=",D)
v = sym.simplify(D)
print("dy/dt=",v)

vel = vt_1 * np.tanh(g_1*t_1/vt_1)

plt.plot(t_1,vel,"--", label = "v(t)")
plt.xlabel("T (s)")
plt.ylabel("v (m/s)")
plt.legend()
plt.show()

#plt.plot(t,y,"--")
#plt.xlabel("T (s)")
#plt.ylabel("X (m)")
#plt.show()