import numpy as np
import matplotlib.pyplot as plt

D=np.array([0.00, 0.735, 1.363, 1.739, 2.805 ,3.814 ,4.458, 4.955, 5.666, 6.329 ])
npontos = len(D)
T=np.arange(0,npontos,1)
plt.scatter(D,T)
plt.xlabel("D (m)")
plt.ylabel("T (s)")
plt.show()