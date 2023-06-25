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

D=np.array([0.1,1.4,1.7,6.5,7.7,10.4,19.5,26.1,26.5,45.9,52.5])
T=np.array([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5])
plt.scatter(D,T)
plt.xlabel("D (cm)")
plt.ylabel("T (s)")
plt.show()

random = regressão(T,D) 