# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 13:42:10 2022

@author: Geraldo Siqueira
"""

import numpy as np
import matplotlib.pyplot as plt

g = 1
l = 1

def F(x):
    return -(g/l)*x

dt = 0.05
dx = 0.01
dw = 0.02
t = np.arange(0,100, dt)
Nt = t.size

#x1
a1 = np.zeros(Nt)
x1 = np.zeros(Nt)
w1 = np.zeros(Nt)

x1[0] = 0 + dx
w1[0] = np.sqrt(2) + dw

#Usando o Método de Verlet para x1
for n in range(1,Nt):
    a1[n-1] = F(x1[n-1])
    x1[n] = x1[n-1] + w1[n-1]*dt + 0.5*a1[n-1]*dt**2
    a1[n] = F(x1[n])
    w1[n] = w1[n-1] + 0.5*(a1[n] + a1[n-1])*dt
    

    
'''
'''
#x2
a2 = np.zeros(Nt)
x2 = np.zeros(Nt)
w2 = np.zeros(Nt)

x2[0] = 0 + dx
w2[0] = np.sqrt(2) - dw

#Usando o Método de Verlet para x2
for n in range(1,Nt):
    a2[n-1] = F(x2[n-1])
    x2[n] = x2[n-1] + w2[n-1]*dt + 0.5*a2[n-1]*dt**2
    a2[n] = F(x2[n])
    w2[n] = w2[n-1] + 0.5*(a2[n] + a2[n-1])*dt

'''
'''
#x3
a3 = np.zeros(Nt)
x3 = np.zeros(Nt)
w3 = np.zeros(Nt)

x3[0] = 0 - dx
w3[0] = np.sqrt(2) + dw

#Usando o Método de Verlet para x3
for n in range(1,Nt):
    a3[n-1] = F(x3[n-1])
    x3[n] = x3[n-1] + w3[n-1]*dt + 0.5*a3[n-1]*dt**2
    a3[n] = F(x3[n])
    w3[n] = w3[n-1] + 0.5*(a3[n] + a3[n-1])*dt
    
'''
'''
#x4
a4 = np.zeros(Nt)
x4 = np.zeros(Nt)
w4 = np.zeros(Nt)

x4[0] = 0 - dx
w4[0] = np.sqrt(4) - dw

#Usando o Método de Verlet para x1
for n in range(1,Nt):
    a4[n-1] = F(x4[n-1])
    x4[n] = x4[n-1] + w4[n-1]*dt + 0.5*a4[n-1]*dt**2
    a4[n] = F(x4[n])
    w4[n] = w4[n-1] + 0.5*(a4[n] + a4[n-1])*dt
    
    

for n in range(1,Nt):
    if n % 15 == 0:
        X=[x1[n],x2[n],x4[n], x3[n], x1[n]]
        W=[w1[n],w2[n],w4[n], w3[n], w1[n]]
        #plt.plot(X,W,'-')
        
#X=[x1[0],x2[0],x4[0], x3[0], x1[0]]
#W=[w1[0],w2[0],w4[0], w3[0], w1[0]]
#plt.title("x1 + x4 em função de t - linearizado")

area = 0.5*(x1*w2 + x2*w3 + x3*w4 + x4*w1) - 0.5*(x2*w1 + x3*w2 + x4*w3 + x1*w4)
plt.plot(t, area)

'''
x5 = x1 + x4
plt.plot(t, x5)
'''
