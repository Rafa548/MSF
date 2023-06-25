# Fres(x) = - m D * | v(x)| * v
# Fres(y) = - m * D * | v(y) | * v (modulo de v ou seja, sqrt(v(x) ** 2 + v(y) ** 2))

import numpy as np
import matplotlib.pyplot as plt


m = 0.057 # gramas
velo = 100 / 3.6 # m/s
veloTerminal = 100 / 3.6 # m/s
convertRate = np.pi/(180) # converter graus para rads
g = 9.8


arrayX = [0]
arrayY = [0]

arrayVelox = [velo * np.cos(10 * convertRate)]
arrayVeloy = [velo * np.sin(10 * convertRate)]

arrayFresX = [- m * (g/(veloTerminal ** 2)) * abs(arrayVelox[0]) * velo]
arrayFresY = [- m * (g/(veloTerminal ** 2)) * abs(arrayVeloy[0]) * velo]

arrayEMec = [1/2 * m * (velo ** 2) + m * g * arrayY[0]]

deltaT = 0.05
arrayTempos = [0]

tempoFinal = 1 # segundo

n = int(1/deltaT)

for i in range(1,n): # sem força de resistencia do ar
    arrayX.append(arrayX[i - 1] + arrayVelox[i - 1] * deltaT)
    arrayY.append(arrayY[i - 1] + arrayVeloy[i - 1] * deltaT)
    arrayVelox.append(arrayVelox[i - 1])
    arrayVeloy.append(arrayVeloy[i - 1] + (- g) * deltaT)
    veloMod = np.sqrt(arrayVelox[i] ** 2 + arrayVeloy[i] ** 2)
    #arrayFresX.append(- m * (g/(veloTerminal ** 2)) * abs(arrayVelox[i]) * veloMod)
    #arrayFresY.append(- m * (g/(veloTerminal ** 2)) * abs(arrayVeloy[i]) * veloMod)
    arrayTempos.append(arrayTempos[i - 1] + deltaT)
    arrayEMec.append(1/2 * m * (veloMod ** 2) + m * g * arrayY[i])



print("{:<20s} {:<20s} {:<20s} {:<20s} {:<10s} {:<10s}".format("X", "Y", "VeloX", "VeloY", "Tempo", "Energia Mec"))
for i in range(len(arrayTempos)):
    print("{:<20f} {:<20f} {:<20f} {:<20f} {:<10f} {:<10f}".format(arrayX[i], arrayY[i], arrayVelox[i], arrayVeloy[i], arrayTempos[i], arrayEMec[i]))

plt.plot(arrayTempos, arrayEMec)
plt.show()


# E(mec) = E(cinetica) * E(potencial gravitica)
