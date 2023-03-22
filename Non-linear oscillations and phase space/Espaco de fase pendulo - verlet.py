# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 09:58:12 2022

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

#Método de Verlet
for n in range(1,Nt):
    a[n-1] = F(o[n-1])
    o[n] = o[n-1] + w[n-1]*dt + 0.5*a[n-1]*dt**2
    a[n] = F(o[n])
    w[n] = w[n-1] + 0.5*(a[n] + a[n-1])*dt
    
    
plt.title("ω x θ - E/E0 = 3 (Verlet)")
plt.ylabel("ω")
plt.xlabel("θ")
plt.plot(o, w, 'r.')