#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[29]:


# Get the page
response = requests.get("https://www.walmart.com/search/?query=water&cat_id=0")
doc = BeautifulSoup(response.text, 'html.parser')


# In[30]:


# Grab all of the titles
title_tags = doc.find_all("div",{"class":"prod-ProductTitle"})
print(title_tags)
# Let's print the first 5
for title in title_tags[:5]:
    print("hello")
    print(title.text.strip())


# In[ ]:





# In[ ]:





# In[35]:


data = {
    'P_QTE_CODE': 'ENG',
    'P_QTE_PGM_CODE': '7500',
    'P_LAST_NAME': 'smith',
    'P_FIRST_NAME': '',
    'P_INITIAL': '',
    'P_LICENSE_NUM': '',
    'P_CITY': '',
    'P_COUNTY': 'LOS ANGELES',
    'P_RECORD_SET_SIZE': '50',
    'Z_ACTION': 'Find'
}

# Get the page
# use .post
# send the data
url = "http://www2.dca.ca.gov/pls/wllpub/WLLQRYNA$LCEV2.ActionQuery"
response = requests.post(url, data=data)
doc = BeautifulSoup(response.content, 'html.parser')
#print(doc.prettify)
# Grab all of the rows
row_tags = doc.find_all('tr')
print(row_tags)
# Let's print the first 5
for row in row_tags[:5]:
    print(row.text.strip())


# In[ ]:




