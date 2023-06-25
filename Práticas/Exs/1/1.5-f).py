import numpy as np
import matplotlib.pyplot as plt

L=np.array([222.0,207.5,194,171.5,153.0,133.0,113.0,92.0])  #distancia
X=np.array([2.3,2.2,2.0,1.8,1.6,1.4,1.2,1.0]) #tempo

#f)
def regressão(L,X):
    x=L
    y=X

    npontos=x.size
    xy=x*y
    x2=x*x
    y2=y*y

    sx=x.sum()
    sy=y.sum()
    sxy=xy.sum()
    sxx=x2.sum()
    syy=y2.sum()

    n=npontos
    rn=n*sxy-sx*sy
    rd=(n*sxx-sx**2)*(n*syy-sy**2)
    r2=rn**2/rd
    r=np.sqrt(r2)
    m=(n*sxy-sx*sy)/(n*sxx-sx**2)
    dm=abs(m)*np.sqrt((1/r**2-1)/(n-2))
    bn=sxx*sy-sx*sxy  
    bd=n*sxx-sx**2
    b=bn/bd
    db=dm*np.sqrt(sxx/n)

    return m,b

r1 = regressão(L,X)  #exemplo
r1_m = r1[0] #m
r1_b = r1[1] #b
x_g = np.arange(80,240,10)     #vetor
l_g = r1_m * x_g + r1_b
plt.plot(x_g,l_g,"--")
plt.scatter(L,X)

X=np.array([2.3,2.2,2.0,1.8,2.3,1.4,1.2,1.0])
r11 = regressão(L,X)
r11_m = r11[0] #m
r11_b = r11[1] #b

plt.scatter(L,X)
plt.xlabel("L (cm)")
plt.ylabel("X (cm)")
x_g = np.arange(80,240,10)     #vetor (entre intervalo 10)
l_g_new = r11_m * x_g + r11_b
plt.plot(x_g,l_g_new,"--")
plt.show()

