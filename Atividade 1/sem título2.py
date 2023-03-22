#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 09:51:36 2022

@author: aluno
"""

import numpy as np
import matplotlib.pyplot as plt

def f(y):
    return -(y*y+1)

#x = np.arange(0, 3, 0.01)
#plt.plot(x, np.exp(x))

dt = 0.1
t = np.arange(0,1, dt)
Nt = t.size
y = np.zeros(Nt)

y[0]=1
plt.plot(0, y, 'r.')
for n in range(1,Nt):
    y = y + f(y)*dt
    plt.plot(t[n], y, 'r.')
    
dt = 0.001
t = np.arange(0,1, dt)
Nt = t.size
y=1
plt.plot(0, y, 'b.')
for n in range(1,Nt):
    y = y + f(y)*dt
    plt.plot(t[n], y, 'b.')