# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 08:44:41 2022

@author: Geraldo Siqueira
"""

import numpy as np
import matplotlib.pyplot as plt
from numba import jit

b = 0.05
O = 0.7
A = 0.6
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
        
        x[n] = x[n-1] + (k1x + 2*k2x + 2*k3x + k4x)/6
        #Para deixar theta entre -pi e pi:
        x[n] = ((x[n]+np.pi)%(2*np.pi))-np.pi
        w[n] = w[n-1] + (k1w + 2*k2w + 2*k3w + k4w)/6
    return x, w

N_Periodos = 50
NP=100
dt = P/NP
t = np.arange(0,N_Periodos*P, dt)
Nt = t.size
x1 = np.zeros(Nt)
w1 = np.zeros(Nt)
x2 = np.zeros(Nt)
w2 = np.zeros(Nt)

#Condições iniciais do pêndulo 1
x1[0] = 0
w1[0] = 0
#Condições iniciais do pêndulo 2
x2[0] = 0
w2[0] = 0.001
rk4(x1, w1, t, dt)
rk4(x2, w2, t, dt)

#Para plotar o mapa de Poincaré   
plt.title("ω(t) para 2 pêndulos (A = 0.6)")
plt.plot(t, w1, 'r')
plt.plot(t, w2, 'b')
plt.xlabel("Tempo")
plt.ylabel("ω")
#plt.xlim([-pi, pi])
#plt.ylim([-3, 3])