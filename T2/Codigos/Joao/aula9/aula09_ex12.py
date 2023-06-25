import numpy as np



m = 75 # kg
g = 9.8 # m/s^2
cres = 0.9 # coeficiente de resistencia do ar
u = 0.004 # coeficiente de atrito
area = 0.3 # da secçao
densidadeAr = 1.225
veloInicial = 1 # m/s
cv = 735.4975 # watts
potenciaCiclista = 0.4 * cv 
deltaT = 0.01
tFinal = 200
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


#print("{:<20s} {:<20s} {:<20s}".format("Posição X", "Velo X", "Acel X"))
#for m in range(len(arrayT)):
#    print("{:<20f} {:<20f} {:<20f}".format(arrayX[m], arrayVeloX[m], arrayAcelX[m]))


valorauxiliar = 2000
index = 0
for l in range(len(arrayT)):
    if abs(2000 - arrayX[l]) < valorauxiliar:
        valorauxiliar = 2000 - arrayX[l]
        index = l
    
print("Andou 2km em {:.2f} segundos".format(arrayT[index]))
