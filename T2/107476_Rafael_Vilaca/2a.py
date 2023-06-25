import numpy as np
import matplotlib.pyplot as plt



m = 60 # kg
g = 9.8 # m/s^2
cres = 0.9 # coeficiente de resistencia do ar
u = 0.01 # coeficiente de atrito
area = 0.5 # da secçao
densidadeAr = 1.225
veloInicial = 0.5 # m/s
cv = 735.4975 # watts
potenciaCiclista = 0.48 * cv 
deltaT = 0.01
tFinal = 50
n = int(tFinal/deltaT)

arrayT = np.zeros(n + 1)
arrayT[0] = 0
arrayX = np.zeros(n + 1)
arrayVeloX = np.zeros(n + 1)
arrayAcelX = np.zeros(n + 1)
arrayX[0] = 0
arrayVeloX[0] = 1
arrayAcelX[0] = ((potenciaCiclista / (arrayVeloX[0])) - (0.5 * densidadeAr * area * cres * (arrayVeloX[0] ** 2)) - (u * m * g))/m


for i in range(1, n + 1):
    arrayT[i] = arrayT[i - 1] + deltaT
    arrayX[i] = arrayX[i - 1] + arrayVeloX[i - 1] * deltaT
    arrayVeloX[i] = arrayVeloX[i - 1] + arrayAcelX[i - 1] * deltaT
    arrayAcelX[i] = ((potenciaCiclista / (arrayVeloX[i])) - (0.5 * densidadeAr * area * cres * (arrayVeloX[i] ** 2)) - (u * m * g))/m


plt.plot(arrayT,arrayVeloX)
plt.show()

