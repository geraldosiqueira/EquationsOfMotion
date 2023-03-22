# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 10:25:22 2022

@author: geral
"""

import numpy as np
import matplotlib.pyplot as plt

t = np. array([0.5, 0.1, 0.01, 0.001, 0.0001])
erros_euler = ([323820880225.128, 12819.276512061435, 62.73213476623485, 4.989965833661492, 0.48813410873276286])
erros_eulerc = ([11.739797244134632, 0.48597488671406897,0.004988299924502115, 4.6513092588629235e-05, 4.840122747040709e-07])
erros_eulerr = ([331.9485866791636, 1.0711416463840884, 0.0019776146296335284, 2.33230144197627e-05, 2.415257771559709e-07])

plt.title("Erro percentual x dt")  
plt.xlabel('dt (s)')
plt.ylabel('Erro Percentual (%)')
plt.loglog(t, erros_euler, 'g.')
plt.loglog(t, erros_eulerc, 'b.')
plt.loglog(t, erros_eulerr, 'y.')
plt.loglog([0,1], [1,1], 'r-')
plt.loglog([0,1], [5,5], 'b-')