# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 09:49:06 2022

@author: Geraldo SIqueira
"""

import numpy as np
import matplotlib.pyplot as plt

def Fx(w):
    return w

def Fw(x):
    return -np.sin(x)

#Runge-Kutta de quarta ordem:
def rk4 (x, w, dt):
    for n in range(1,Nt):
        k1x = Fx(w[n-1])*dt
        k1w = Fw(x[n-1])*dt
        
        k2x = Fx(w[n-1] + 0.5*k1w)*dt
        k2w = Fw(x[n-1] + 0.5*k1x)*dt
        
        k3x = Fx(w[n-1] + 0.5*k2w)*dt
        k3w = Fw(x[n-1] + 0.5*k2x)*dt
        
        k4x = Fx(w[n-1] + k3w)*dt
        k4w = Fw(x[n-1] + k3x)*dt
        
        x[n] = x[n-1] + (k1x + 2*k2x + 2*k3x + k4x)/6
        w[n] = w[n-1] + (k1w + 2*k2w + 2*k3w + k4w)/6
    return x, w
   
dt = 0.01
t = np.arange(0,50, dt)
Nt = t.size
x = np.zeros(Nt)
w = np.zeros(Nt)

x[0] = 0
w[0] = 1
rk4(x, w, dt)
   
plt.plot(x, w, 'r.')
