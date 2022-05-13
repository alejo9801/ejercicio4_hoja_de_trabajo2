#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt


# In[18]:


data = pd.read_csv('C:/Users/TEMP/Documents/datos1.csv')
data


# In[19]:


linear_model=smf.ols(formula ='Ganancia ~ Tiemvisual', data = data).fit()


# In[20]:


linear_model.params


# Ganancia =28098.256735 + Tiemvisual * 954.412044

# In[26]:


linear_model.pvalues


# In[27]:


linear_model.rsquared


# In[31]:


linear_model.summary()


# In[34]:


Ganancia_pred= linear_model.predict(pd.DataFrame(data['Tiemvisual']))
Ganancia_pred


# In[37]:


data.plot(kind= 'scatter',x='Tiemvisual',y='Ganancia')
plt.plot(pd.DataFrame(data['Tiemvisual']), Ganancia_pred, c='green', linewidth=3)


# In[ ]:




