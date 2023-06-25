import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

#FUNCTIONS
"=============================================================================="
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
"=============================================================================="
"=============================================================================="

#MAIN
#------------------------------------
# Gravidade
g = 9.8

# Massa
m = 0.5

# k e b
k = 2
a = -0.1
b = 0.02

# Tempo inicial e final
t0 = 0
tf = 50

# Velocidade terminal
# vtx = 6.8

# Posição e Velocidade inicial
xeq = 0
x0 = 1.5
vx0 = 0.5

# dt incremento do tempo e n numero de intervalos
dt = 0.001
n = int((tf - t0) / dt)

# Vetor tempo (n+1 para garantir que nao falta o ultimo dado (Ex: t[10]))
t = np.linspace(t0, tf, n + 1)

# Vetor velocidade (empty e não zeros para não alterar
# muito o resultado se faltar analisar um dado)
x = np.empty(n + 1)
vx = np.empty(n + 1)
ax = np.empty(n + 1)

Ep = np.empty(n+1)
Ec = np.empty(n+1)
Em = np.empty(n+1)

xrk4 = np.empty(n + 1)
vxrk4 = np.empty(n + 1)

# Introduzir x0 e v0 nos vetores da posição e velocidade
x[0] = x0
vx[0] = vx0
# xrk4[0] = xx0
# vxrk4[0] = vx0

#Euler-crommer
for i in range(n):
    ax[i]=-(k/m)*x[i]-3*(a/m)*x[i]**2 + 4*(b/m)*x[i]**3 ##Mudar
    vx[i + 1] = vx[i] + ax[i] * dt
    x[i + 1] = x[i] + vx[i+1] * dt
    
    Ep[i]= 0.5*k*x[i]**2 + a*x[i]**3 - b*x[i]**4
    Ec[i]= 0.5*m*vx[i]**2
    
    Em[i] = Ec[i] + Ep[i]

#LAST VALUES
Ep[n]= 0.5*k*x[n]**2 + a*x[n]**3 - b*x[n]**4
Ec[n]= 0.5*m*vx[n]**2
 
Em[n] = Ec[n] + Ep[n]

#b)
EM = np.median(Em)
EC = np.median(Ec)
EP = np.median(Ep)

print("Mechanical:")
print("Em = {:0.4f} m".format(EM))

#GRAPHS
#================================================
#ENERGIA POTENCIAL
plt.plot(x, Ep, "-m", label = "x")
plt.grid()
plt.title("Variacao da Eneria Potencial")

plt.xlabel("x(m)")
plt.ylabel("Ep(J)")

plt.ylim(0,4)   

plt.legend()
plt.show()
"================================================"

#LEI DO MOVIMENTO
plt.plot(t, x, "-r", label = "x")
plt.grid()
plt.title("Lei do movimento")

plt.xlabel("t(s)")
plt.ylabel("x(m)")

plt.legend()
plt.show()
"================================================"
"================================================"
#ENERGIA MECANICA
plt.plot(t, Em, "-b", label = "x")
plt.grid()
plt.title("Energia Mecanica")

#POINTS
# plt.plot(t00, W00, "ok", label ="Wres0.0")
# plt.plot(t04, W04, "or", label ="Wres0.4")
# plt.plot(t08, W08, "ob", label ="Wres0.8")

plt.xlabel("t(s)")
plt.ylabel("Em(J)")

plt.ylim(0,30)

plt.legend()
plt.show()
"================================================"
