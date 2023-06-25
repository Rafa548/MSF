# 1. Uma bola de futebol é chutada com velocidade de 100 km/h, a fazer um ângulo de 10º com o campo (horizontal).
# e) Considere agora a resistência do ar. A força de resistência do ar ao movimento da bola é:

# 𝐹𝑥(𝑟𝑒𝑠) = −𝑚 𝐷 |v|𝑣𝑥
# 𝐹𝑦(𝑟𝑒𝑠) = −𝑚 𝐷 |v|𝑣𝑦
# em que 𝐷 = 𝑔/𝑣𝑇^2 , e a velocidade terminal é 𝑣𝑇 = 100 km/h. Atualize o seu programa de modo a considerar a
# força de resistência do ar. Faça o gráfico da altura em função da distância percorrida na horizontal.

import numpy as np
import matplotlib.pyplot as plt

convertRate = np.pi/(180)
veloInicial = 100 / 3.6
g = 9.8
veloTerminal = 100 / 3.6
constD = g / (veloTerminal ** 2)
# angulo = 10º
deltaT = 0.001
n = int(1/deltaT)

arrayTempos = np.zeros(n + 1) # n + 1 zeros para ter indices de 0 a n, com n intervalos
arrayX = np.zeros(n + 1)
arrayY = np.zeros(n + 1)
arrayX[0] = 0
arrayY[0] = 0

arrayVeloX = np.zeros(n + 1)
arrayVeloY = np.zeros(n + 1)
arrayAcelX = np.zeros(n + 1)
arrayAcelY = np.zeros(n + 1)

arrayTempos[0] = 0
arrayVeloX[0] = veloInicial * np.cos(16 * convertRate)
arrayVeloY[0] = veloInicial * np.sin(16 * convertRate)
arrayAcelX[0] = (- constD * veloInicial * arrayVeloX[0])
arrayAcelY[0] = -g + (- constD * veloInicial * arrayVeloY[0]) 


for i in range(1, n + 1):
    arrayTempos[i] = arrayTempos[i - 1] + deltaT
    arrayVeloX[i] = arrayVeloX[i - 1]
    arrayX[i] = arrayX[i - 1] + arrayVeloX[i - 1] * deltaT
    arrayY[i] = arrayY[i - 1] + arrayVeloY[i - 1] * deltaT
    arrayVeloX[i] = arrayVeloX[i - 1] + arrayAcelX[i - 1] * deltaT
    arrayVeloY[i] = arrayVeloY[i - 1] + arrayAcelY[i - 1] * deltaT
    velo = np.sqrt((arrayVeloX[i] ** 2) + (arrayVeloY[i] ** 2))
    arrayAcelX[i] = -constD * velo * arrayVeloX[i]
    arrayAcelY[i] = -g - constD * velo * arrayVeloY[i]


plt.plot(arrayX, arrayY)
plt.show()

for i in range(1,n+1):
    if((arrayX[i]) > (20-deltaT) and (arrayX[i-1]) < (20+deltaT)):            
        print("A_1 -> ",arrayY[i])      
        print("A_2 -> ",arrayY[i+1])




