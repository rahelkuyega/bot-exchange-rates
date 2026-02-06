#!/usr/bin/env python
# coding: utf-8

# In[1]:
g
from bs4 import BeautifulSoup as bs

import numpy as np
import pandas as pd
import requests


# # to notify the specific organization we are human

# In[2]:


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
}


# In[3]:


link="https://www.bot.go.tz/ExchangeRate/excRates"


# In[4]:


try:
    response = requests.get(link,headers=headers)

except:
    ("error occurred")


# In[4]:


import requests
response=requests.get(link,headers=headers)
if response.status_code == 200:
    print("your response accepted")

else:
    ("your response not accepted")


# #fetch html structure

# In[5]:


#send the response to get the html structure
html=response.text


# In[5]:


#send the response to get the html structure
html=response.text


# In[6]:


#to disply the html structure
html_structure=bs(html,"html.parser")
html_structure


# In[7]:


# to fetch existing table
table=html_structure.find("table")
table


# In[8]:


rows=[tr for tr in table.find_all("tr")]


# In[9]:


print(rows)


# In[10]:


headers=[th.get_text(strip=True) for th in table.find_all("th")]


# In[11]:


headers1=pd.Series(headers).unique().tolist()


# In[12]:


headers1 = headers1[1:]


# In[13]:


headers1


# In[14]:


rac=[]
for row in rows:
    
    cell=row.find_all("td")
    if len(cell)>0:
        
        currency=cell[1].text.strip()
        buying=cell[2].text.strip()
        selling=cell[3].text.strip()
        mean=cell[4].text.strip()
        transaction_date=cell[5].text.strip()
        rac.append([currency,buying,selling,mean,transaction_date])


        


# In[15]:


rac


# In[16]:


df=pd.DataFrame(rac,columns = headers1)


# In[17]:


df


# In[18]:


df.columns


# In[19]:


print(df.dtypes)


# In[20]:


df.head()


# In[21]:


df.info()


# In[29]:


#concert buying,selling and mean into numeric
num_col=["Buying","Selling","Mean"]
for col in num_col:
    df[col]=pd.to_numeric(df[col],errors="coerce")


# In[23]:


df["Transaction Date"]=pd.to_datetime(df["Transaction Date"],format="%d-%b-%y",errors="coerce")


# In[24]:


#to add the extra column thats consider the current data
df["extracted_at"]=pd.Timestamp.now()


# In[25]:


df


# In[26]:


df["source_url"]="https://www.bot.go.tz/ExchangeRate/excRates"


# In[30]:


#to store data into csv
df.to_csv("bot_exchange_rates.csv", index=False)



# In[31]:


import os
os.getcwd()

