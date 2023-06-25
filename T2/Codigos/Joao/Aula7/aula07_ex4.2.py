# 4. Numa partida de ténis, muitas vezes a bola é batida de modo a adquirir rotação, num eixo horizontal e perpendicular à
# velocidade. Calcule a trajetória da bola, quando parte da posição inicial (-10,1,0) com a velocidade 130 km/h, a fazer um ângulo de
# 10º com a horizontal e no sentido positivo dum eixo horizontal OX. A bola de ténis tem a massa 57 g, o diâmetro 67 mm e no ar tem
# a velocidade terminal 100 km/h. Calcule a altura máxima e o alcance (quando bate em y=0) da trajetória da bola, quando
# a) A rotação é nula.

import numpy as np
import matplotlib.pyplot as plt


arrayX = [-10]
arrayY = [1]
arrayZ = [0]
angulo = 10 * np.pi/(180) # radianos
m = 0.057 # kg
raio = 67 * (10 ** -3)/2 # metros
g = 9.8
# Forças (sem rotação): Peso e força de resistência do ar


veloTerminal = 100 / 3.6 # m/s
veloInicial = 130 / 3.6 # m/s
constanteD = g/(veloTerminal ** 2)



# OBJETIVO: Calcular altura máxima e alcance


# Velocidade sobre z é nula e não há nenhuma força para a variar


arrayVeloX = [veloInicial * np.cos(angulo)]
arrayVeloY = [veloInicial * np.sin(angulo)]
arrayAcelX = [- constanteD * veloInicial * arrayVeloX[0]]
arrayAcelY = [(- constanteD * veloInicial * arrayVeloY[0]) - (g)]

arrayTempos = [0] # so para ajudar no grafico

deltaT = 0.01
n = int(2/deltaT)



for i in range(1,n):
    velo = np.sqrt(arrayVeloX[i - 1] ** 2 + arrayVeloY[i - 1] ** 2)
    arrayX.append(arrayX[i - 1] + arrayVeloX[i - 1] * deltaT)
    arrayY.append(arrayY[i - 1] + arrayVeloY[i - 1] * deltaT)
    arrayVeloX.append(arrayVeloX[i - 1] + arrayAcelX[i - 1] * deltaT)
    arrayVeloY.append(arrayVeloY[i - 1] + arrayAcelY[i - 1] * deltaT)
    arrayAcelX.append(- constanteD * abs(velo) * arrayVeloX[i])
    arrayAcelY.append(- constanteD * abs(velo) * arrayVeloY[i] - (g))
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


plt.plot(arrayX, arrayY) # trajetoria
plt.show()



# b) A rotação é descrita por 𝜔 = (0, 0, +100) rad/s


# Força(Magnus) = 1/2 * densidade do ar * raio * (W X Z)

# w = (0,0,100) rad/s
# v = (vx, vy, 0)

