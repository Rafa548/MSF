# 3. Uma bola de ténis é batida junto ao solo (posição inicial 𝑦 = 0)com a velocidade 100 km/h, a fazer um ângulo de
# 10º com a horizontal e no sentido positivo dum eixo horizontal OX, sendo OY eixo vertical.
# b) Considerando a resistência do ar, calcule a energia mecânica nos três instantes
# 𝑡0 = 0, 𝑡1 = 0.4 s e 𝑡2 = 0.8 s.

import numpy as np
import matplotlib.pyplot as plt


massa = 0.057 # kg
veloTerminal = 100 / 3.6 # m/s
veloInicial = 100 / 3.6 # m/s
convertRate = np.pi/(180) # converter graus para rads
g = 9.8 # m/s^2
constanteD = (g) / (veloTerminal ** 2)

deltaT = 0.001 # passo do metodo de euler
tempoFinal = 1 # sujeito a alteração
n = int(1/deltaT) # numero de iterações do metodo de euler

# inicialização dos arrays necessários
arrayX = np.zeros(n + 1)
arrayY = np.zeros(n + 1)
arrayVeloX = np.zeros(n + 1)
arrayVeloY = np.zeros(n + 1)
arrayFresx = np.zeros(n + 1)
arrayFresy = np.zeros(n + 1)
arrayAcelX = np.zeros(n + 1)
arrayAcelY = np.zeros(n + 1)
arrayEMec = np.zeros(n + 1)
arrayT = np.zeros(n + 1)

# valores iniciais
arrayX[0] = 0 # redundante mas na boa
arrayY[0] = 0 # redundante mas ok
arrayVeloX[0] = np.cos(10 * convertRate) * veloInicial
arrayVeloY[0] = np.sin(10 * convertRate) * veloInicial
arrayFresx[0] = - massa * constanteD * arrayVeloX[0] * veloInicial
arrayFresy[0] = - massa * constanteD * abs(arrayVeloY[0]) * veloInicial
arrayAcelX[0] = arrayFresx[0]/massa
arrayAcelY[0] = (- g + arrayAcelY[0]) / massa
arrayEMec[0] = 1/2 * massa * (veloInicial ** 2) + massa * g * arrayY[0]


# calculo de todos os valores

for i in range(1,n + 1): # começar em 1 porque já tenho os valores para 0
    arrayT[i] = arrayT[i - 1] + deltaT
    arrayX[i] = arrayX[i - 1] + arrayVeloX[i - 1] * deltaT
    arrayY[i] = arrayY[i - 1] + arrayVeloY[i - 1] * deltaT
    arrayVeloX[i] = arrayVeloX[i - 1] + arrayAcelX[i - 1] * deltaT
    arrayVeloY[i] = arrayVeloY[i - 1] + arrayAcelX[i - 1] * deltaT
    veloMod = np.sqrt(arrayVeloX[i] ** 2 + arrayVeloY[i] ** 2)
    arrayFresx[i] = - massa * constanteD * arrayVeloX[i] * veloMod
    arrayFresy[i] = - massa * constanteD * arrayVeloY[i] * veloMod
    arrayAcelX[i] = arrayFresx[i]/massa
    arrayAcelY[i] = (-g + arrayFresy[i])/massa
    arrayEMec[i] = 1/2 * massa * (veloMod ** 2) + massa * g * arrayY[i]



# Energia Mecânica no instante 0s:

print("Energia mecânica no instante 0s: ", arrayEMec[0])

# Energia mecânica no instante 0.4s:

print("Energia mecânica no instante 0.4s: ", arrayEMec[int(0.4/deltaT)])

# Energia mecânica no instante 0.8s:

print("Energia mecânica no instante 0.8s:", arrayEMec[int(0.8/deltaT)])

for k in range(n + 1):
    print(arrayY[k], arrayVeloY[k])



