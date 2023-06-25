import math
import numpy as np
import matplotlib.pyplot as plt

vT = 6.8
G = 9.8

x =  np.linspace(0.0, 2.0, num=10, endpoint=True)
y = (vT**2/G)*np.log(math.cosh(G*x/vT))




