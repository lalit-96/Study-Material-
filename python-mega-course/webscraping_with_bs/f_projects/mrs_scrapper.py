#!/usr/bin/env python
# coding: utf-8

# In[55]:


import requests
from bs4 import BeautifulSoup


# In[ ]:





# In[65]:


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

url = "https://maharerait.mahaonline.gov.in/SearchList/Search"
response = requests.post(url, data=data)
doc = BeautifulSoup(response.content, 'html.parser')
#print(doc)


# In[ ]:





# In[66]:


try:

    sr=doc.find("div",{"id":"DivBind"})
    if sr.find("label").get_text().strip()=="No Records Found":
        print("No Records Found")
    else:
        print("SEARCH RESULT")
        static_url="https://maharerait.mahaonline.gov.in"
        urls=[]
        #sr=doc.find("div",{"id":"DivBind"})
        tbody=sr.find("table").find("tbody")

        for row  in tbody.find_all("tr"):
            url=row.find_all("td")[4].find("a")['href']
            url=static_url+url
            urls.append(url)
except:
        print("Something went wrong.......")


# In[67]:


len(urls)


# In[ ]:





# In[ ]:


__RequestVerificationToken: -xiy9Jc2lbte6mW_lMb4Hg6hvuZ5IWKc_Yf_RokaUcuTphpKFTYmqcrST_lvaeMF2DwVUelEOUQ36Jny3N7KQdtFK0hTKD60IsoC8-1lJ8E1


# In[72]:



data={   
"__RequestVerificationToken": "-xiy9Jc2lbte6mW_lMb4Hg6hvuZ5IWKc_Yf_RokaUcuTphpKFTYmqcrST_lvaeMF2DwVUelEOUQ36Jny3N7KQdtFK0hTKD60IsoC8-1lJ8E1",
"Type":"Promoter",
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
"hdnState": 27,
"District": "",
"Taluka": "",
"Village": "",
"CompletionDate_From":"", 
"hdnfromdate": "",
"CompletionDate_To":"", 
"hdntodate": "",
"PType": "",
"hdnPType":"",
"TotalRecords": 6432,
"CurrentPage": 2,
"TotalPages": 129,
"Command": "Next"
}
url = "https://maharerait.mahaonline.gov.in/SearchList/Search"
response = requests.post(url, data=data)
doc = BeautifulSoup(response.content, 'html.parser')
      


# In[69]:


print(doc.prettify)


# In[73]:


try:

    sr=doc.find("div",{"id":"DivBind"})
    if sr.find("label").get_text().strip()=="No Records Found":
        print("No Records Found")
    else:
        print("SEARCH RESULT")
        static_url="https://maharerait.mahaonline.gov.in"
        urls=[]
        #sr=doc.find("div",{"id":"DivBind"})
        tbody=sr.find("table").find("tbody")

        for row  in tbody.find_all("tr"):
            url=row.find_all("td")[4].find("a")['href']
            url=static_url+url
            urls.append(url)
except:
        print("Something went wrong.......")


# In[74]:


urls[1]


# # Final Looping different pages

# In[ ]:





# In[ ]:





# In[ ]:





# In[83]:


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict)
del(dict['Name']); # remove entry with key 'Name'

print(dict)
dict.clear();     # remove all entries in dict
print(dict)
del(dict) ;        # delete entire dictionary


# In[ ]:





# In[ ]:





# In[ ]:





# In[79]:



    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




