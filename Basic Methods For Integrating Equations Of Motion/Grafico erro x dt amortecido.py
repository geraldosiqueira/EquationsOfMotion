# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 13:25:45 2022

@author: geral
"""

import numpy as np
import matplotlib.pyplot as plt

t = np. array([0.5, 0.1, 0.01, 0.001, 0.0001])
erros_euler = ([533296600677.8566, 13583.961458990441, 70.83807368778733, 10.35579560858904, 5.638604168052858])
erros_eulerc = ([5.641999487180032, 3.89767127375867, 5.01779155358697, 5.116505047497518, 5.126039058748407])
erros_eulerr = ([72.584444706233, 4.584380950690026, 5.139006305884112, 5.129819020845253, 5.127379310564158])

plt.title("Erro percentual x dt - amortecido")  
plt.xlabel('dt (s)')
plt.ylabel('Erro Percentual (%)')
plt.loglog(t, erros_euler, 'g.')
plt.loglog(t, erros_eulerc, 'b.')
plt.loglog(t, erros_eulerr, 'y.')
plt.loglog([0,1], [1,1], 'r-')
plt.loglog([0,1], [5,5], 'b-')