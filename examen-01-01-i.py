# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as ss
import matplotlib.pyplot as plt


# In[2]:


df = pd.ExcelFile('C:\\Users\\if686748\\Downloads\\Base_de_datos_terapia_agresividad.xlsx')
df.sheet_names
df = df.parse(df.sheet_names[0], header=0)


# In[5]:


df = df.iloc[:,68:75] #ultimas 7


# ## a) Medidas de tendencia central

# In[6]:


df.mean()


# In[7]:


df.median()


# In[8]:


df.mode()


# ##  b) Interpretación 
# 
# La variable impulsi_disfun es la que presenta mayor promedio respecto al resto, comparandolo con la mediana que es dos unidades mayor se puede decir que la distribución tendrá un sesgo respecto de la media. 

# # c) Medidas dispersión univariantes

# In[9]:


df.var()


# In[10]:


df.std()


# # d) Interpretacion var y dev
# 
# No solo Impulsi_disfun es la variable con mayor promedio, sino que tambien con mayor desviación estándar, es decir que es la que más se aleja del promedio que otras, sin embargo no se aleja más que otras. Se esperaria que respecto de la media de dicha variable se encuentren la myoria de los datos en un rago contruido con la media y la desviación. 

# # e) Medidas de dispersión bivariantes

# In[17]:


df.corr()


# In[14]:


df.cov()


# # f) Variables con correlación inversa?
# 
# Las variables (Ira,empatía), (Ira,Impulsi_funcio) y (Ira,Impulsi_disfun) están inversamente correlacionadas.

# # g) Variables con mayor y menor correlación
# 
# Mayor correlación (Impulsi_disf,Impulsi_funcio) y menor correlacion (Ira,Empatia)

# # h) Si correlación = 0 se concluye independencia? 
# 
# Si la correlación es igual a cero significa que no tienen relación lineal, sin embargo no significa independencia. 

# # i) Estimadores de maxima versolimilitud (Media y desv) 

# In[23]:


impulsi_disf = df.iloc[:,3]


# In[25]:


impulsi_disf_estimadores = impulsi_disf.sample(30)


# In[26]:


impulsi_disf.mean()


# In[27]:


impulsi_disf_estimadores.mean()


# In[28]:


impulsi_disf.std()


# In[29]:


impulsi_disf_estimadores.std()


# In[36]:


plt.title('impulsi_disf')
plt.hist(impulsi_disf, bins = 10)


# In[39]:


media,desviacion = ss.norm.fit(impulsi_disf)


# In[47]:


n = impulsi_disf.count()
freqs, edges,_ = ss.binned_statistic(impulsi_disf,impulsi_disf,statistic='count')


# In[48]:


def fd(i):
    return n*(ss.norm.cdf(edges[i], loc = media, scale = desviacion) - 
             ss.norm.cdf(edges[i-1], loc = media, scale = desviacion))
expected = [fd(i) for i in range(1,len(edges))]


# In[43]:


plt.bar(np.arange(len(freqs)),
       freqs,alpha=0.5,Color='b')
plt.bar(np.arange(len(expected)),
       expected, alpha = 0.5, Color = 'r')
plt.legend(('datos','normal'))
plt.show

