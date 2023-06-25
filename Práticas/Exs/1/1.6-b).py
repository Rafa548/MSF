import numpy as np
import matplotlib.pyplot as plt
def regressão(x,y):

    npontos=x.size
    xy=x*y
    x2=x*x
    y2=y*y

    sx=x.sum()
    sy=y.sum()
    sxy=xy.sum()
    sxx=x2.sum()
    syy=y2.sum()

    print("sx,sy,sxy,sxx,syy")
    print(sx,sy,sxy,sxx,syy)

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

    print('m +/-dm= ',m ,"+/-", dm)
    print('b +/-db= ',b ,"+/-",db)
    print('r2= ',r2)

    return m,b
D=np.array([0.00, 0.735, 1.363, 1.739, 2.805 ,3.814 ,4.458, 4.955, 5.666, 6.329 ])
npontos = len(D)
T=np.arange(0,npontos,1)
plt.scatter(D,T)
plt.xlabel("D (m)")
plt.ylabel("T (s)")
#plt.show()

random = regressão(T,D)




