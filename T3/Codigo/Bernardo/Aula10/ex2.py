# -*- coding: utf-8 -*-
"""
Created on Mon May 30 16:52:04 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.0001

t = np.arange(0, 50+dt,dt)
k = 1
m = 1

v = np.zeros(t.size)
x = np.zeros(t.size)

v1 = np.zeros(t.size)
x1 = np.zeros(t.size)

f = np.zeros(t.size)
x[0] = 4
v[0] = 0
x1[0] = 4
v1[0] = 0

for i in range(t.size-1):
    f[i] =  -k * x[i]
    a = f[i]/m
    v[i+1] = v[i] + a*dt
    x[i+1] = x[i] + v[i]*dt


#fig1, ax = plt.subplots(1, 2, figsize=(13,6), layout="constrained")

#ax[0].plot(t,x)

for i in range(t.size-1):
    f[i] =  -k * x1[i]
    a = f[i]/m
    v1[i+1] = v1[i] + a*dt
    x1[i+1] = x1[i] + v1[i+1]*dt
    

plt.plot(t,x1)
#ax[1].plot(t,x1)

firstdivision = x1[30000:100000]
seconddivision = x1[110000:160000]

print(np.amax(firstdivision))
print(np.amax(seconddivision))

index1, = np.where(x1 == np.amax(firstdivision))
index2, = np.where(x1 == np.amax(seconddivision))
print(index1)
print(index2)
plt.plot(t[index1], np.amax(firstdivision), "bx")
plt.plot(t[index2], np.amax(seconddivision), "bx")

print("tempo entre cristas ->", t[index2]-t[index1])

xtest1 = [3,3]
ytest1 = [-5,5]

xtest2 = [10,10]
ytest2 = [-5,5]

xtest3 = [16,16]
ytest3 = [-5,5]
plt.plot(xtest1,ytest1)
plt.plot(xtest2,ytest2)
plt.plot(xtest3,ytest3)
