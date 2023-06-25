import numpy as np
import matplotlib.pyplot as plt

arrayX = [-10]
arrayY = [1]
arrayZ = [0]
angulo = 10 * np.pi/(180) # radianos
m = 0.057 # kg
raio = (67 * (10 ** -3))/2 # metros
g = 9.8
# Forças (sem rotação): Peso e força de resistência do ar


veloTerminal = 100 / 3.6 # m/s
veloInicial = 130 / 3.6 # m/s
constanteD = g/(veloTerminal ** 2)
arrayTempos = [0]


arrayVeloX = [veloInicial * np.cos(angulo)]
arrayVeloY = [veloInicial * np.sin(angulo)]

deltaT = 0.001
n = int(2/deltaT)

# b) A rotação é descrita por 𝜔 = (0, 0, +100) rad/s


# Força(Magnus) = 1/2 * densidade do ar * raio * (W X Z) // W x V = 0 neste caso

# w = (0,0,100) rad/s
# v = (vx, vy, 0)       



densidadeAr = 1.225 # kg/m^3
FmagnusX = (1/2 * densidadeAr * raio * (- 100 * arrayVeloX[0]) * np.pi * (raio ** 2))/m
FmagnusY = (1/2 * densidadeAr * raio * (100 * arrayVeloY[0]) * np.pi * (raio ** 2))/m


arrayAcelX = [(- m * constanteD * abs(arrayVeloX[0]) * veloInicial) + FmagnusX] # FALTA MUDAR A VELOCIDADE PARA O MODULO DELA!!
arrayAcelY = [(- m * constanteD * abs(arrayVeloY[0]) * veloInicial) - g + FmagnusY] # DAÍ O ERRO CÃO!


for i in range(1, n):
    velo = np.sqrt(arrayVeloX[i - 1] ** 2 + arrayVeloY[i - 1] ** 2)
    arrayX.append(arrayX[i - 1] + arrayVeloX[i - 1] * deltaT)
    arrayY.append(arrayY[i - 1] + arrayVeloY[i - 1] * deltaT)
    arrayVeloX.append(arrayVeloX[i - 1] + arrayAcelX[i - 1] * deltaT)
    arrayVeloY.append(arrayVeloY[i - 1] + arrayAcelY[i - 1] * deltaT)
    arrayAcelX.append((- m * constanteD * abs(arrayVeloX[0]) * velo) + (1/2 * densidadeAr * raio * np.pi * (raio ** 2) * (- 100 * arrayVeloX[i - 1]))/m)
    arrayAcelY.append((- m * constanteD * abs(arrayVeloY[0]) * velo) - g + (1/2 * densidadeAr * raio * np.pi * (raio ** 2) *  (100 * arrayVeloY[i - 1]))/m)
    arrayTempos.append(arrayTempos[i - 1] + deltaT)


print("{:<20s} {:<20s} {:<20s} {:<20s} {:<20s} {:<20s} {:<20s}".format("X", "Y", "VeloX", "VeloY", "ForçaResX", "ForçaResY", "Tempo"))
for i in range(len(arrayTempos)):
    print("{:<20f} {:<20f} {:<20f} {:<20f} {:<20f} {:<20f} {:<20f}".format(arrayX[i], arrayY[i], arrayVeloX[i], arrayVeloY[i], arrayAcelX[i], arrayAcelY[i], arrayTempos[i]))

# Calculo de altura máximo
minVeloY = arrayVeloY[0] # variavel para encontrar a velocidade minima sob o eixo de subir/descer

for i in range(len(arrayTempos)):
    if (abs(arrayVeloY[i])) < minVeloY:
        minVeloY = arrayVeloY[i]

indexMinVeloY = arrayVeloY.index(minVeloY)

alturaMax = arrayY[indexMinVeloY] # A altura máxima é o valor de y no qual a velocidade está mais perto de zero.

# Calculo de alcance
minPosiY = arrayY[0]

for i in range(len(arrayTempos)):
    if abs(arrayY[i]) < minPosiY:
        minPosiY = arrayY[i]


indexMinPosiY = arrayY.index(minPosiY)

# O alcance é o instante em que a altura é 0
alcance = arrayX[indexMinPosiY]

print("Alcance: ", alcance)
print("Altura máxima: ", alturaMax)


plt.plot(arrayX, arrayY)
plt.show()