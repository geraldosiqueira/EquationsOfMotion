# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 13:46:39 2022

@author: Geraldo Siqueira 
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from numba import jit

b = 0.05
O = 0.7
A = 0.7
#Período => P = 2pi/Omega
P = 2*np.pi/O

@jit
def Fx(x,w,t):
    return w

@jit
def Fw(x,w,t):
    return -b*w - np.sin(x) + A*np.cos(O*t)

#Runge-Kutta de quarta ordem:
@jit
def rk4 (x, w, t, dt):
    for n in range(1,Nt):
        k1x = Fx(x[n-1], w[n-1], t[n-1])*dt
        k1w = Fw(x[n-1], w[n-1], t[n-1])*dt
        
        k2x = Fx(x[n-1] + 0.5*k1x, w[n-1] + 0.5*k1w, t[n-1] + 0.5*dt)*dt
        k2w = Fw(x[n-1] + 0.5*k1x, w[n-1] + 0.5*k1w, t[n-1] + 0.5*dt)*dt
        
        k3x = Fx(x[n-1] + 0.5*k2x, w[n-1] + 0.5*k2w, t[n-1] + 0.5*dt)*dt
        k3w = Fw(x[n-1] + 0.5*k2x, w[n-1] + 0.5*k2w, t[n-1] + 0.5*dt)*dt
        
        k4x = Fx(x[n-1] + k3x, w[n-1] + k3w, t[n-1] + dt)*dt
        k4w = Fw(x[n-1] + k3x, w[n-1] + k3w, t[n-1] + dt)*dt
        
        x[n] = x[n-1] + (k1x + 2*k2x + 2*k3x +  k4x)/6
        #Para deixar theta entre -pi e pi:
        x[n] = ((x[n]+np.pi)%(2*np.pi))-np.pi
        w[n] = w[n-1] + (k1w + 2*k2w + 2*k3w + k4w)/6
    return x, w


N_Periodos = 1000000
NP=100
dt = P/NP
t = np.arange(0,N_Periodos*P, dt)
Nt = t.size
x = np.zeros(Nt)
w = np.zeros(Nt)

x[0] = 1
w[0] = 0
rk4(x, w, t, dt)

#Para plotar o mapa de Poincaré   
plt.title("Mapa de Poincaré para A = 0.9")
plt.plot(x[2*Nt//3:Nt-1:NP], w[2*Nt//3:Nt-1:NP], 'r,')
plt.xlim([-pi, pi])
plt.ylim([-3, 3])