# 3. Uma bola de ténis é batida junto ao solo (posição inicial 𝑦 = 0)com a velocidade 100 km/h, a fazer um ângulo de
# 10º com a horizontal e no sentido positivo dum eixo horizontal OX, sendo OY eixo vertical.

# c) Considerando a resistência do ar, calcule o trabalho realizado pela força de resistência do ar até às posições nos
# três instantes
# 𝑡0 = 0, 𝑡1 = 0.4 s e 𝑡2 = 0.8 s.

# Use a aproximação trapezoidal para calcular os integrais. A velocidade terminal da bola de ténis é 100 km/h. AS
# massa da bola é 57 g.

import numpy as np
import matplotlib.pyplot as plt


massa = 0.057 # kg
veloTerminal = 100 / 3.6 # m/s
veloInicial = 140 / 3.6 # m/s
convertRate = np.pi/(180) # converter graus para rads
g = 9.8 # m/s^2
constanteD = (g) / (veloTerminal ** 2)

deltaT = 0.001 # passo do metodo de euler
tempoFinal = 2 # sujeito a alteração
n = int(tempoFinal/deltaT) # numero de iterações do metodo de euler (numero de intervalos)

# inicialização dos arrays necessários
arrayX = np.zeros(n + 1) # n + 1 pois vai até ao indice n
arrayY = np.zeros(n + 1)
arrayVeloX = np.zeros(n + 1)
arrayVeloY = np.zeros(n + 1)
arrayFresx = np.zeros(n + 1)
arrayFresy = np.zeros(n + 1)
arrayAcelX = np.zeros(n + 1)
arrayAcelY = np.zeros(n + 1)
arrayEMec = np.zeros(n + 1)
arrayTrabalho = np.zeros(n + 1)
arrayT = np.zeros(n + 1)
arrayFunc = np.zeros(n + 1)

# valores iniciais
arrayX[0] = 0 # redundante mas na boa
arrayY[0] = 0 # redundante mas ok
arrayVeloX[0] = np.cos(7 * convertRate) * veloInicial                                                 # ******** Angulo aq
arrayVeloY[0] = np.sin(7 * convertRate) * veloInicial                                                  # ******* e aq
arrayFresx[0] = - massa * constanteD * arrayVeloX[0] * veloInicial
arrayFresy[0] = - massa * constanteD * arrayVeloY[0] * veloInicial
arrayAcelX[0] = arrayFresx[0]/massa
arrayAcelY[0] = (- g + arrayAcelY[0]) / massa
arrayEMec[0] = 1/2 * massa * (veloInicial ** 2) + massa * g * arrayY[0]
arrayTrabalho[0] = 0
arrayT[0] = 0
arrayFunc[0] = arrayVeloX[0] * arrayFresx[0] + arrayVeloY[0] * arrayFresy[0]


for i in range(1, n + 1): # começar em 1 porque já tenho os valores para 0
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
    # Tentativa Integral
    arrayFunc[i] = arrayVeloX[i] * arrayFresx[i] + arrayVeloY[i] * arrayFresy[i]
    # Terminar Integral
    arrayTrabalho[i] = (deltaT * 0.5 * ((arrayFresx[i - 1] * arrayVeloX[i - 1]) + (arrayFresx[i] * arrayVeloX[i]))) + (deltaT * 0.5 * ((arrayFresy[i - 1] * arrayVeloY[i - 1]) + (arrayFresy[i] * arrayVeloY[i])))



print("trabalho realizado pela Força de Resistência do ar no instante t = 0.9s: ", np.sum(arrayTrabalho[0:int(0.9/deltaT) + 1]))


# Integral

print("Integral 0.9s: ", deltaT * ((arrayFunc[0] + arrayFunc[int(0.9/deltaT)]) * 0.5 + np.sum(arrayFunc[1:int(0.9/deltaT)])))


# Os dois metodos funcionam (entendo melhor o dos trabalhos a cada instante, mas o integral também funciona)

plt.plot(arrayT, arrayFresx)
plt.show()