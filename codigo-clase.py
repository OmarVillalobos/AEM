# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%
data = pd.read_csv('C:\\Users\\if686748\\AppData\\Local\\Temp\\StudentsPerformance.csv')
data =  data.iloc[:,5:8]

#%% media aritmetica
media = data.mean()


#%% mediana
mediana = data.median()


#%% moda 
moda = data.mode()
print(moda.iloc[0,0])

#%% varianza
varianza = data.var()

#%% desv estandar
desviacion = data.std()

#%% covarianza
covarianza = data.cov()

plt.figure()
plt.scatter(data['reading score'], data['writing score'])
plt.xlabel('reading')
plt.ylabel('writing')
plt.show()
#%%
#%% plot
plt.figure()
plt.scatter(np.arange(1000), data['math score'])
plt.plot(np.arange(1000), media[0]*np.ones(1000), c='r')
plt.plot(np.arange(1000), mediana[0]*np.ones(1000), c='b')
plt.plot(np.arange(1000), moda.iloc[0,0]*np.ones(1000), c='y')
#plt.plot(np.arange(1000), media[0]+varianza[0]*np.ones(1000), c='m')
#plt.plot(np.arange(1000), media[0]-varianza[0]*np.ones(1000), c='m')
plt.plot(np.arange(1000), media[0]+desviacion[0]*np.ones(1000), c='k')
plt.plot(np.arange(1000), media[0]-desviacion[0]*np.ones(1000), c='k')
plt.show()
