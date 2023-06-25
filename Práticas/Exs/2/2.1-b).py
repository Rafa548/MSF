import numpy as np
import matplotlib.pyplot as plt

v0_km_h = 70
v0_m_s = 70/3.6
a = 2

#t = np.linspace(0,30,300)
#xc = v0_m_s * t         #posição
#xp = 1/2 * a * t**2

x = 2 * v0_m_s**2/a #posiçao onde se intercetao
t = 2 * v0_m_s/a  #tempo onde se intercetao

#plt.plot(t,xc,"--",label="Carro A")
#plt.plot(t,xp,"--",label="Carro Patrulha")
#plt.xlabel("T (s)")
#plt.ylabel("X (m)")
print(x)
print(t)
#plt.legend()
#plt.show()