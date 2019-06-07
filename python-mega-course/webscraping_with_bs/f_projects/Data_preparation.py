#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# # Create a DataFrame from Lists oR list of lists

# In[2]:


data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
df


# # Create a DataFrame from Dict of ndarrays / Lists

# In[5]:


data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
df


# # Create a DataFrame from List of Dicts

# In[6]:


data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20,'d':23 }]
df = pd.DataFrame(data)
df


# # The following example shows how to create a DataFrame with a list of dictionaries, row indices, and column indices.

# In[15]:



data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20},{'c': 5, 'b': 10}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, columns=['a', 'b','c'])

#With two column indices with one index with other name
df2 = pd.DataFrame(data, columns=['a', 'b1'])
print(df1)
df2


# # Dictionary

# In[ ]:





# In[ ]:




