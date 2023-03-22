# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 08:36:56 2022

@author: Geraldo Siqueira
"""

import numpy as np
import matplotlib.pyplot as plt

g = 1
l = 1

def F(o):
    return -(g/l)*np.sin(o)

dt = 0.05
t = np.arange(0,50, dt)
Nt = t.size
a = np.zeros(Nt)
o = np.zeros(Nt)
w = np.zeros(Nt)

o[0] = 0
w[0] = np.sqrt(6)

#Usando Euler-Richardson
for n in range(1,Nt):
    a[n-1] = F(o[n-1])
    wm = w[n-1] + a[n-1]*(dt/2)
    om = o[n-1] + w[n-1]*(dt/2)
    am = F(om)
    w[n] = w[n-1] + am*dt
    o[n] = o[n-1] + wm*dt

'''
calculando diferentes valores de energia E/E0 = 0.5, 1, 2 e 3
'''

plt.title("ω x θ - E/E0 = 3 (Euler-Richardson)")
plt.ylabel("ω")
plt.xlabel("θ") 
plt.plot(o, w, 'r.')
