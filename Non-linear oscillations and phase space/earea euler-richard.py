# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 10:46:51 2022

@author: Geraldo Siqueira
"""

import numpy as np
import matplotlib.pyplot as plt

g = 1
l = 1

def F(x):
    return -(g/l)*np.sin(x)

dt = 0.05
dx = 0.01
dw = 0.02
t = np.arange(0,20, dt)
Nt = t.size

#x1
a1 = np.zeros(Nt)
x1 = np.zeros(Nt)
w1 = np.zeros(Nt)

x1[0] = 0 + dx
w1[0] = np.sqrt(2) + dw

#Usando Euler-Richardson para x1
for n in range(1,Nt):
    a1[n-1] = F(x1[n-1])
    wm1 = w1[n-1] + a1[n-1]*(dt/2)
    xm1 = x1[n-1] + w1[n-1]*(dt/2)
    am1 = F(xm1)
    w1[n] = w1[n-1] + am1*dt
    x1[n] = x1[n-1] + wm1*dt

    
'''
'''
#x2
a2 = np.zeros(Nt)
x2 = np.zeros(Nt)
w2 = np.zeros(Nt)

x2[0] = 0 + dx
w2[0] = np.sqrt(2) - dw

#Usando Euler-Richardson para x2
for n in range(1,Nt):
    a2[n-1] = F(x2[n-1])
    wm2 = w2[n-1] + a2[n-1]*(dt/2)
    xm2 = x2[n-1] + w2[n-1]*(dt/2)
    am2 = F(xm2)
    w2[n] = w2[n-1] + am2*dt
    x2[n] = x2[n-1] + wm2*dt

'''
'''
#x3
a3 = np.zeros(Nt)
x3 = np.zeros(Nt)
w3 = np.zeros(Nt)

x3[0] = 0 - dx
w3[0] = np.sqrt(2) + dw

#Usando Euler-Richardson para x3
for n in range(1,Nt):
    a3[n-1] = F(x3[n-1])
    wm3 = w3[n-1] + a3[n-1]*(dt/2)
    xm3 = x3[n-1] + w3[n-1]*(dt/2)
    am3 = F(xm3)
    w3[n] = w3[n-1] + am3*dt
    x3[n] = x3[n-1] + wm3*dt
    
'''
'''
#x4
a4 = np.zeros(Nt)
x4 = np.zeros(Nt)
w4 = np.zeros(Nt)

x4[0] = 0 - dx
w4[0] = np.sqrt(2) - dw

#Usando Euler-Richardson para x4
for n in range(1,Nt):
    a4[n-1] = F(x4[n-1])
    wm4 = w4[n-1] + a4[n-1]*(dt/2)
    xm4 = x4[n-1] + w4[n-1]*(dt/2)
    am4 = F(xm4)
    w4[n] = w4[n-1] + am4*dt
    x4[n] = x4[n-1] + wm4*dt
    
    

for n in range(1,Nt):
    if n % 15 == 0:
        X=[x1[n],x2[n],x4[n], x3[n], x1[n]]
        W=[w1[n],w2[n],w4[n], w3[n], w1[n]]
        #plt.plot(X,W,'-')
        
#X=[x1[0],x2[0],x4[0], x3[0], x1[0]]
#W=[w1[0],w2[0],w4[0], w3[0], w1[0]]
plt.title("Área em função do tempo (Euler-Richardson)")

area = 0.5*(x1*w2 + x2*w3 + x3*w4 + x4*w1) - 0.5*(x2*w1 + x3*w2 + x4*w3 + x1*w4)
plt.plot(t, area)
