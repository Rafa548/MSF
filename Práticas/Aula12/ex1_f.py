
import matplotlib.pyplot as plt
import numpy as np

dt = 0.001

k = 1
m = 1
Fz = 7.5
b = 0.05
wf = 1 #rad
w = np.sqrt(k/m)
xeq=0

t = np.arange(0, 400+dt, dt)

arrayx = []
tempos = []
periodo = []
x = np.zeros(t.size)
v = np.zeros(t.size)
a = np.zeros(t.size)
x[0] = -2
v[0] = -4
Em = np.zeros(t.size)
ind = np.transpose([0 for i in range(1000)])                        ####################### importante pra coefecientes

for i in range(t.size-1):
    a[i] = (-k/m)*x[i]-(b*v[i])/m + Fz*np.cos(wf *t[i])/m 
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i]+v[i+1]*dt
    #Em[i] = m*(0.5*v[i]**2 + 0.5*(k*x[i]**2-xeq**2))


#Em[t.size-1] = m*(0.5*v[t.size-1]**2 + 0.5*(k*x[t.size-1]**2-xeq**2))

for i in range(t.size-1):
    if (x[i-1]<x[i]>x[i+1] and i>0 and t[i]>250):   #mudar 250 para o estacionário que se vê no grafico
        #arrayx.append(x[i])
        #tempos.append(t[i])
        countMax = countMax+1
        ind[countMax] = int[i]      #tem de ser int

t0=ind[countMax-1]
t1=ind[countMax]
for i in range(15):
    af, bf = abfourier(tempo,x,t0,t1,i)
    afo[i] = af
    a
#for i in range(0,len(tempos)-1):
    #periodo.append(tempos[i+1]-tempos[i])           


#print("Periodo ->",np.mean(periodo))
#print("Amplitude ->" ,np.mean(arrayx))

#plt.plot(t,x)
#plt.show()

#plt.plot(t,Em)
#plt.show()



def abfourier(tp,xp,it0,it1,nf):
#
# cálculo dos coeficientes de Fourier a_nf e b_nf
#       a_nf = 2/T integral ( xp cos( nf w) ) dt   entre tp(it0) e tp(it1)
#       b_nf = 2/T integral ( xp sin( nf w) ) dt   entre tp(it0) e tp(it1)    
# integracao numerica pela aproximação trapezoidal
# input: matrizes tempo tp   (abcissas)
#                 posição xp (ordenadas) 
#       indices inicial it0
#               final   it1  (ao fim de um período)   
#       nf índice de Fourier
# output: af_bf e bf_nf  
# 
    dt=tp[1]-tp[0]
    per=tp[it1]-tp[it0]
    ome=2*np.pi/per

    s1=xp[it0]*np.cos(nf*ome*tp[it0])
    s2=xp[it1]*np.cos(nf*ome*tp[it1])
    st=xp[it0+1:it1]*np.cos(nf*ome*tp[it0+1:it1])
    soma=np.sum(st)
    
    q1=xp[it0]*np.sin(nf*ome*tp[it0])
    q2=xp[it1]*np.sin(nf*ome*tp[it1])
    qt=xp[it0+1:it1]*np.sin(nf*ome*tp[it0+1:it1])
    somq=np.sum(qt)
    
    intega=((s1+s2)/2+soma)*dt
    af=2/per*intega
    integq=((q1+q2)/2+somq)*dt
    bf=2/per*integq
    return af,bf