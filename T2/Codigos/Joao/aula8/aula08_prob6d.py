# 6. Uma mola exerce uma força 𝐹𝑥 = −𝑘 𝑥 𝑡 , em que 𝑘 é a constante elástica da mola, num corpo de massa 𝑚.
# Considere 𝑘 = 1 N/m e 𝑚 = 1 kg.

# E(mec) = E(cinetica) + E(potencial elastica) 
# E(potencial elastica) = 1/2 * k * x^2

# x(t) = A * cos(wt + k)
# v(t) = - A * w * sin(wt + k)
# a(t) = - w^2 * x(t)
# x(0) = 4
# v(0) = 0 logo, 0 = A*w*sin(wt+k), ou seja, 0 = sin(wt + k), então k = 0 ou pi 
# portanto 4 = A * cos (w*0 + k)
# Para k = 0: 4 = A * cos(0) ou seja 4 = A, portanto A = 4

import numpy as np
import matplotlib.pyplot as plt


massa = 1 # kg
k = 1 # N/m
w = np.sqrt(k/massa) # rad/s
deltaT = 0.01 # intervalo de tempo entre cada 
tempoFinal = 20 # segundos
amplitude = 4 # metros
faseInicial = 0 
n = int(tempoFinal/deltaT) # numero de intervalos para os metodos


# Definir arrays (para Euler e Euler-cromer tal como o exercicio pede)
arrayXEuler = np.zeros(n + 1) # n + 1 para ir até ao index n
arrayXEulerC = np.zeros(n + 1)
arrayVeloEuler = np.zeros(n + 1)
arrayVeloEulerC = np.zeros(n + 1)
arrayAcelEuler = np.zeros(n + 1)
arrayAcelEulerC = np.zeros(n + 1)
arrayEnergiaEuler = np.zeros(n + 1)
arrayEnergiaEulerC = np.zeros(n + 1)
arrayT = np.zeros(n + 1)

arrayXEuler[0] = 4 # diz no enunciado
arrayXEulerC[0] = 4
arrayVeloEuler[0] = 0
arrayVeloEulerC[0] = 0
arrayAcelEuler[0] = - (w ** 2) * arrayXEuler[0]
arrayEnergiaEuler[0] = 1/2 * massa * arrayVeloEuler[0] ** 2 + (1/2 * k * (arrayXEuler[0] ** 2))
arrayEnergiaEulerC[0] = 1/2 * massa * arrayVeloEulerC[0] ** 2 + (1/2 * k * (arrayXEulerC[0] ** 2))
arrayT[0] = 0



# Metodo de Euler

for i in range(1, n + 1): # 1 a n + 1 pois exclui o n + 1, para ir até ao index n
    arrayXEuler[i] = arrayXEuler[i - 1] + arrayVeloEuler[i - 1] * deltaT
    arrayVeloEuler[i] = arrayVeloEuler[i - 1] + arrayAcelEuler[i - 1] * deltaT
    arrayAcelEuler[i] = - (w ** 2) * arrayXEuler[i]
    arrayEnergiaEuler[i] = 1/2 * massa * (arrayVeloEuler[i] ** 2) + (1/2 * k * (arrayXEuler[i] ** 2))
    arrayT[i] = arrayT[i - 1] + deltaT

# Metodo de Euler - Cromer: (calcular a velocidade antes da posição, e usar a velocidade atual em vez da anterior)

for ii in range(1, n + 1):
    arrayVeloEulerC[ii] = arrayVeloEulerC[ii - 1] + arrayAcelEulerC[ii - 1] * deltaT
    arrayXEulerC[ii] = arrayXEulerC[ii - 1] + arrayVeloEulerC[ii] * deltaT # está aqui a unica diferença
    arrayAcelEulerC[ii] = - (w ** 2) * arrayXEulerC[ii]
    arrayEnergiaEulerC[ii] = (1/2 * massa * (arrayVeloEulerC[ii] ** 2)) + (1/2 * k * (arrayXEulerC[ii] ** 2))

#print("{:<20s} {:<20s} {:<20s} {:<20s}".format("Energia Euler", "Energia Euler Cromer", "Acel Euler", "Acel EulerC"))
#for i in range(len(arrayT)):
#    print("{:<20f} {:<20f} {:<20f} {:<20f}".format(arrayEnergiaEuler[i], arrayEnergiaEulerC[i], arrayAcelEuler[i], arrayAcelEulerC[i]))

print("{:<20s} {:<20s} {:<20s} {:<20s}".format("Energia EulerC", "Posição EulerC", "Velo EulerC", "Acel EulerC"))
for m in range(len(arrayT)):
    print("{:<20f} {:<20f} {:<20f} {:<20f}".format(arrayEnergiaEulerC[m], arrayXEulerC[m], arrayVeloEulerC[m], arrayAcelEulerC[m]))



# Gráficos:

#Euler
plt.subplot(1, 2, 1)
plt.xlabel("Tempo")
plt.ylabel("Posição")
plt.plot(arrayT, arrayXEuler, label="Euler")
plt.plot(arrayT, arrayXEulerC, label="Euler-Cromer")
plt.legend(loc="upper left")

#Euler-Cromer
plt.subplot(1, 2, 2)
plt.xlabel("Tempo")
plt.ylabel("Energia")
plt.plot(arrayT, arrayEnergiaEuler, label="Euler")
plt.plot(arrayT, arrayEnergiaEulerC, label="Euler-Cromer")
plt.legend(loc="upper left")


plt.show()

# Tal como é possivel ver, o metodo de Euler-Cromer consegue conservar energia mecânica e o de Euler não, pois aumenta