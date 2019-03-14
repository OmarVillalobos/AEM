
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt 
from sklearn import datasets, linear_model 
from sklearn.model_selection import train_test_split


# In[4]:


boston = datasets.load_boston() 
boston.feature_names


# In[5]:


X = boston.data[:,5] 
Y = boston.target


# In[28]:


X = np.reshape(X,(506,1)) 
Y = np.reshape(Y,(506,1)) 
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.2)


# In[29]:


lr = linear_model.LinearRegression() 
lr.fit(X_train, Y_train) 
Y_predi = lr.predict(X_test)


# In[30]:


len(X)


# In[47]:


lr.intercept_[0]


# In[31]:


lr.coef_[0][0]


# In[32]:


np.std(X)


# In[33]:


np.std(Y)


# In[48]:


np.mean(X)


# In[43]:


t_1 = lr.coef_[0][0]/(np.std(Y)/(np.sqrt(len(X))*np.std(X)))


# In[44]:


t_1


# t_1 > 1.96 para alfa = 0.05, por lo tanto se rechaza Ho 

# In[49]:


t_0 = lr.intercept_[0]/((np.std(Y)/np.sqrt(len(X)))*(np.sqrt(1+((np.mean(X))**2)/np.std(X)**2)))


# In[51]:


np.abs(t_0)

