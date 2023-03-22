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

def F(x):
    return -k*x

dt = 0.001
t = np.arange(0,50, dt)
Nt = t.size
a = np.zeros(Nt)
x = np.zeros(Nt)
v = np.zeros(Nt)
Amp_e = np.array([])
Amp_ec = np.array([])
Amp_er = np.array([])

x[0] = 1
v[0] = 0

#Méodo de Euler
for n in range(1,Nt):
    a[n-1] = F(x[n-1])/m
    v[n] = v[n-1] + a[n-1]*dt
    x[n] = x[n-1] + v[n-1]*dt
    if v[n]*v[n-1]<0:
        Amp_e = np.append(Amp_e, (x[n]+x[n-1])/2)
    

plt.title("Método de Euler")
'''    
plt.plot(t, x, 'b.')
plt.plot(t, v, 'r.')
'''
'''
erro_euler = np.abs(np.abs(Amp_e) - 1)
plt.plot(erro_euler, 'g.')
print(np.max(erro_euler)*100)
'''
plt.plot(v, x, 'r.')

#Méodo de Euler-Cromer
for n in range(1,Nt):
    a[n-1] = F(x[n-1])/m
    v[n] = v[n-1] + a[n-1]*dt
    x[n] = x[n-1] + v[n]*dt
    if v[n]*v[n-1]<0:
        Amp_ec = np.append(Amp_ec, (x[n]+x[n-1])/2)

#plt.title("Método de Euler-Cromer")
'''  
plt.plot(t, x, 'b.')
plt.plot(t, v, 'r.')
'''
'''
erro_eulerc = np.abs(np.abs(Amp_ec) - 1)
plt.plot(erro_eulerc, 'b.')
print(np.max(erro_eulerc)*100)
'''
#plt.plot(v, x, 'r.')
K = 0.5*v*v
U = 0.5*k*x*x
E = K+U


#Méodo de Euler-Richardon
for n in range(1,Nt):
    a[n-1] = F(x[n-1])/m
    vm = v[n-1] + a[n-1]*(dt/2)
    xm = x[n-1] + v[n-1]*(dt/2)
    am = F(xm)/m
    v[n] = v[n-1] + am*dt
    x[n] = x[n-1] + vm*dt
    if v[n]*v[n-1]<0:
        Amp_er = np.append(Amp_er, (x[n]+x[n-1])/2)
    

#plt.title("Método de Euler-Richard")
'''
erro_eulerr = np.abs(np.abs(Amp_er) - 1)
plt.plot(erro_eulerr, 'r.')
print(np.max(erro_eulerr)*100)
'''
#plt.plot(v, x, 'r.')


'''
plt.plot(t, K, 'y.')
plt.plot(t, U, 'g.')
plt.plot(t, E, 'r.')
'''