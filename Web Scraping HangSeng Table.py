#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


# Create an URL object
url = 'https://www.investing.com/indices/hong-kong-40-futures-historical-data'

# create object page
page = requests.get(url)

print(page)


# In[4]:


# create object page
page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

print(page)


# In[5]:


# parser-lxml = change html to Python friendly format
# Obtain page's information

soup = BeautifulSoup(page.text, 'html' )

soup


# In[6]:


# Obtain information from tag <table>
table1 = soup.find('table', id='curr_table')

table1


# In[7]:


# Obtain every title of columns with tag <th>

headers=[]
for i in table1.find_all('th'):
    title = i.text  
    headers.append(title)


# In[8]:


headers


# In[10]:


mydata = pd.DataFrame(columns=headers)


# In[11]:


#create a for loop to fill mydata
for j in table1.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row  = [i.text for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row


# In[12]:


mydata


# In[13]:


#export to csv
mydata.to_excel('HangSengHistoricalData.xlsx', index=False)


# In[ ]:




