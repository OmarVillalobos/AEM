
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as ss
import matplotlib.pyplot as plt


# In[6]:


df = pd.read_csv('C:\\Users\\if686748\\Downloads\\Altura.csv')
df.head()


# In[7]:


plt.title('Alturas')
plt.hist(df.Altura, bins = 10)


# In[9]:


# Ajuste de distribucion normal
media,desviacion = ss.norm.fit(df.Altura)


# In[10]:


# Realizar muestreo de la variable continua
n = df.Altura.count()
freqs, edges,_ = ss.binned_statistic(df.Altura,df.Altura,statistic='count')


# In[12]:


edges


# In[13]:


def fd(i):
    return n*(ss.norm.cdf(edges[i], loc = media, scale = desviacion) - 
             ss.norm.cdf(edges[i-1], loc = media, scale = desviacion))
expected  = [fd(i) for i in range(1,len(edges))]


# In[16]:


plt.bar(np.arange(len(freqs)),
       freqs,alpha=0.5,Color='b')
plt.bar(np.arange(len(expected)),
       expected, alpha = 0.5, Color = 'r')
plt.legend(('datos','normal'))
plt.show

