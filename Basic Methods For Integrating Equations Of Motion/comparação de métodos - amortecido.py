#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 13:19:16 2022

@author: Geraldo Siqueira
"""

import numpy as np
import matplotlib.pyplot as plt

k = 1
m = 1
ni = 0.1

def F(x, v):
    return -k*x - ni*v

dt = 0.1
t = np.arange(0,100, dt)
Nt = t.size
a = np.zeros(Nt)
x = np.zeros(Nt)
v = np.zeros(Nt)
Amp_e = np.array([])
Amp_ec = np.array([])
Amp_er = np.array([])
tempo_er = np.array([])
tempo_ec = np.array([])
tempo_e = np.array([])

x[0] = 1
v[0] = 0


#Méodo de Euler
for n in range(1,Nt):
    a[n-1] = F(x[n-1], v[n-1])/m
    v[n] = v[n-1] + a[n-1]*dt
    x[n] = x[n-1] + v[n-1]*dt
    if v[n]*v[n-1]<0:
        Amp_e = np.append(Amp_e, (x[n]+x[n-1])/2)
        tempo_e = np.append(tempo_e, 1+(n*dt))



#plt.title("Método de Euler")
'''    
plt.plot(t, x, 'b.')
plt.plot(t, v, 'r.')


tempo2_e = np.exp(-(0.1/2)*tempo_e)
erro_euler = np.abs(np.abs(Amp_e) - tempo2_e)/tempo2_e
plt.plot(erro_euler, 'g.')
print(np.max(erro_euler)*100)
'''

#plt.plot(v, x, 'g.')


#Méodo de Euler-Cromer
for n in range(1,Nt):
    a[n-1] = F(x[n-1], v[n-1])/m
    v[n] = v[n-1] + a[n-1]*dt
    x[n] = x[n-1] + v[n]*dt
    if v[n]*v[n-1]<0:
        Amp_ec = np.append(Amp_ec, (x[n]+x[n-1])/2)
        tempo_ec = np.append(tempo_ec, 1+(n*dt))


#plt.title("Método de Euler-Cromer")
'''
plt.plot(t, x, 'b.')
plt.plot(t, v, 'r.')


tempo2_ec = np.exp(-(0.1/2)*tempo_ec)
erro_eulerc = np.abs(np.abs(Amp_ec) - tempo2_ec)/tempo2_ec
plt.plot(erro_eulerc, 'b.')
print(np.mean(erro_eulerc)*100)
'''
#plt.plot(v, x, 'g.')


#Méodo de Euler-Richardon
for n in range(1,Nt):
    a[n-1] = F(x[n-1], v[n-1])/m
    vm = v[n-1] + a[n-1]*(dt/2)
    xm = x[n-1] + v[n-1]*(dt/2)
    am = F(xm, vm)/m
    v[n] = v[n-1] + am*dt
    x[n] = x[n-1] + vm*dt
    if v[n]*v[n-1]<0:
        Amp_er = np.append(Amp_er, (x[n]+x[n-1])/2)
        tempo_er = np.append(tempo_er, 1+(n*dt))
   
'''
#z = -np.exp(-(0.1/2)*t)
#plt.plot(t,z)
ze = np.exp(-(0.1/2)*t)
plt.plot(t,ze)
'''
  

plt.title("Método de Euler-Richard")
'''
plt.plot(t, x, 'b.')
#plt.plot(t, v, 'r.')


tempo2_er = np.exp(-(0.1/2)*tempo_er)
erro_eulerr = np.abs(np.abs(Amp_er) - tempo2_er)/tempo2_er
#plt.plot(erro_eulerr, 'r.')
print(np.mean(erro_eulerr)*100)
'''
plt.plot(v, x, 'g.')


K = 0.5*v*v
U = 0.5*k*x*x
E = K+U


'''
plt.plot(t, K, 'y.')
plt.plot(t, U, 'g.')
plt.plot(t, E, 'r.')
'''