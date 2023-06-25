import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,4,100)
vt = 6.8
g = 9.8

y = (vt**2/g)*np.log(np.cosh(g*t/vt))

plt.plot(t,y,"--")
plt.xlabel("T (s)")
plt.ylabel("X (m)")
plt.show()