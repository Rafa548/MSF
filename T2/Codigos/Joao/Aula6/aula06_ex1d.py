# 1. Uma bola de futebol é chutada com velocidade de 100 km/h, a fazer um ângulo de 10º com o campo (horizontal).
# d) Desenvolva um programa que obtenha a lei do movimento e a lei da velocidade em função do tempo, usando o
# método de Euler. Tem confiança que o seu programa está correto?

import numpy as np

convertRate = np.pi/(180)
veloInicial = 100 / 3.6
# angulo = 10º
deltaT = 0.01
n = int(10/deltaT)
arrayTempos = np.zeros(n + 1) # n + 1 zeros para ter indices de 0 a n, com n intervalos
arrayX = np.zeros(n + 1)
arrayY = np.zeros(n + 1)
arrayX[0] = 0
arrayY[0] = 0
arrayVeloX = np.zeros(n + 1)
arrayVeloY = np.zeros(n + 1)
arrayTempos[0] = 0
arrayVeloX[0] = veloInicial * np.cos(10 * convertRate)
arrayVeloY[0] = veloInicial * np.sin(10 * convertRate)
g = 9.8
ay = -g


for i in range(1, n + 1):
    arrayTempos[i] = arrayTempos[i - 1] + deltaT
    arrayVeloX[i] = arrayVeloX[i - 1]
    arrayX[i] = arrayX[i - 1] + arrayVeloX[i - 1] * deltaT
    arrayY[i] = arrayY[i - 1] + arrayVeloY[i - 1] * deltaT
    vy = arrayVeloY[i - 1] + ay * deltaT
    arrayVeloY[i] = vy
    if arrayY[i] < 0:
        break


print("{:<20s} {:<20s} {:<20s} {:<20s}".format("Posição X", "Posição Y", "Velo X", "Velo Y"))
for m in range(len(arrayTempos)):
    print("{:<20f} {:<20f} {:<20f} {:<20f}".format(arrayX[m], arrayY[m], arrayVeloX[m], arrayVeloY[m]))
