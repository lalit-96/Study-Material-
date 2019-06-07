#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import re


# In[2]:


data={   
"__RequestVerificationToken": "zBn9eHJuR3tfsAXytw0D9hSYSzA1PJ5d0m7Qn_7z0ng_e23GWtoQPLSY9emRZzcgEVpBRRgp_SIi82PNm0QIlUVZ-SmVEu0I6VxDa2dkNU01",
"ID": 0,
"pageTraverse": 1,
"Project":"" ,
"hdnProject":"", 
"Promoter": "",
"hdnPromoter":"", 
"AgentName": "",
"hdnAgent": "",
"CertiNo": "",
"hdnCertiNo":"", 
"State": 27,
"Division": 5,
"hdnDivision":"", 
"hdnDistrict": "",
"hdnProject": "",
"hdnDTaluka": "",
"hdnVillage": "",
"hdnState": "",
"District": "",
"Taluka": "",
"Village": "",
"CompletionDate_From":"", 
"hdnfromdate": "",
"CompletionDate_To":"", 
"hdntodate": "",
"PType": "",
"hdnPType":"", 
"btnSearch": "Search"
      }


# In[3]:


urls=[]


# In[4]:


try:
    response = requests.post("https://maharerait.mahaonline.gov.in/SearchList/Search", data=data)
    home = BeautifulSoup(response.content, 'html.parser')
    sr=home.find("div",{"id":"DivBind"})
    if sr.find("label").get_text().strip()=="No Records Found":
        print("No Records Found")
    else:
        static_url="https://maharerait.mahaonline.gov.in"

        #sr=doc.find("div",{"id":"DivBind"})
        tbody=sr.find("table").find("tbody")

        for row  in tbody.find_all("tr"):
            url=row.find_all("td")[4].find("a")['href']
            url=static_url+url
            urls.append(url)
except:
    print("Something went wrong.......")


# In[ ]:





# In[5]:


pagination=home.find("ul",{"class":"pagination clearfix col-sm-12 col-xs-12"})
TotalRecords=pagination.find_all("li")[0].find("input")['value']
TotalPages=re.findall(r'\d+',pagination.find_all("li")[1].get_text() )[0]


# In[ ]:





# In[6]:


del(data["btnSearch"])
data['"TotalRecords"']=int(TotalRecords)
data["CurrentPage"]=1
data["TotalPages"]= int(TotalPages)
data["Command"]="Next"


# In[ ]:





# In[7]:


for page in range(1,10,1):
    data['CurrentPage']=page
    try:
        response = requests.post("https://maharerait.mahaonline.gov.in/SearchList/Search", data=data)
        doc = BeautifulSoup(response.content, 'html.parser')
        sr=doc.find("div",{"id":"DivBind"})
        if sr.find("label").get_text().strip()=="No Records Found":
            print("No Records Found")
        else:
            static_url="https://maharerait.mahaonline.gov.in"

            #sr=doc.find("div",{"id":"DivBind"})
            tbody=sr.find("table").find("tbody")

            for row  in tbody.find_all("tr"):
                url=row.find_all("td")[4].find("a")['href']
                url=static_url+url
                urls.append(url)
    except:
        print("Something went wrong.......")


# In[8]:


len(urls)


# In[ ]:





# In[ ]:




