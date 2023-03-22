# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 09:14:23 2022

@author: Geraldo Siqueira
"""

import numpy as np
import matplotlib.pyplot as plt

b = 0.05
O = 0.7
A = 0.6

#((x+np.pi)%2*np.pi)-np.pi

def Fx(x,w,t):
    return w

def Fw(x,w,t):
    return -b*w - np.sin(x) + A*np.cos(O*t)

#Runge-Kutta de quarta ordem:
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


dt = 0.05
t = np.arange(0,300, dt)
Nt = t.size
x = np.zeros(Nt)
w = np.zeros(Nt)
Amp = np.array([])
T = np.array([])

x[0] = 1
w[0] = 0
rk4(x, w, t, dt)

#plotando os gráficos de θ x ω e de θ x tempo
fig, ax = plt.subplots(2)
ax[0].plot(x, w, '.')
ax[0].set_xlabel("θ")
ax[0].set_ylabel("ω")
ax[1].plot(t, x)
ax[1].set_xlabel("tempo")
ax[1].set_ylabel("θ")
'''
#plotando os gráficos de θ x ω e de θ x tempo parte estável
fig, ax = plt.subplots(2)
ax[0].plot(x[Nt//2:Nt-1], w[Nt//2:Nt-1], '.')
ax[0].set_xlabel("θ")
ax[0].set_ylabel("ω")
ax[1].plot(t[Nt//2:Nt-1], x[Nt//2:Nt-1], '.')
ax[1].set_xlabel("tempo")
ax[1].set_ylabel("θ")
'''
#Para estimar o tempo transiente
for i in range(1,Nt):
    if w[i]*w[i-1]<0:
        Amp = np.append(Amp, np.abs((x[i]+x[i-1])/2))
        T = np.append(T, t[i])
        
'''
plt.plot(T, Amp)
plt.title("Amplitudes máximas em função do tempo")
plt.xlabel("Tempo")
plt.ylabel("Módulo da Amplitude")
'''