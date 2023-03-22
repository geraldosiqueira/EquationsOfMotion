#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 13:19:16 2022

@author: aluno
"""

import numpy as np
import matplotlib.pyplot as plt

k = 1
m = 1

def F(x):
    return -k*x

dt = 0.1
t = np.arange(0,20, dt)
Nt = t.size
a = np.zeros(Nt)
x = np.zeros(Nt)
v = np.zeros(Nt)

x[0] = 1
v[0] = 0

#Méodo de Euler
for n in range(1,Nt):
    a[n-1] = F(x[n-1])/m
    v[n] = v[n-1] + a[n-1]*dt
    x[n] = x[n-1] + v[n-1]*dt
    
plt.title("Método de Euler")    
plt.plot(t, x, 'b.')
plt.plot(t, v, 'r.')

 
'''
#Méodo de Euler-Cromer
for n in range(1,Nt):
    a[n-1] = F(x[n-1])/m
    v[n] = v[n-1] + a[n-1]*dt
    x[n] = x[n-1] + v[n]*dt
   
plt.title("Método de Euler-Cromer")
plt.plot(t, x, 'b.')
plt.plot(t, v, 'r.')
'''

'''
#Méodo de Euler-Richardon
for n in range(1,Nt):
    a[n-1] = F(x[n-1])/m
    vm = v[n-1] + a[n-1]*(dt/2)
    xm = x[n-1] + v[n-1]*(dt/2)
    am = F(xm)/m
    v[n] = v[n-1] + am*dt
    x[n] = x[n-1] + vm*dt
plt.title("Método de Euler-Richard")
plt.plot(t, x, 'b.')
plt.plot(t, v, 'r.')
'''
'''
K = 0.5*v*v
U = 0.5*  k*x*x
E = K+U

plt.plot(t, K, 'y.')
plt.plot(t, U, 'g.')
plt.plot(t, E, 'r.')
'''