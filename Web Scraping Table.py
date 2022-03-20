# i follow tutorial at this link 
# https://medium.com/analytics-vidhya/how-to-scrape-a-table-from-website-using-python-ce90d0cfb607

#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[3]:


# Create an URL object
url = 'https://www.worldometers.info/coronavirus/'

# create object page
page = requests.get(url)

print(page)


# In[4]:


# parser-lxml = change html to Python friendly format
# Obtain page's information

soup = BeautifulSoup(page.text, 'html' )

soup


# In[5]:


# Obtain information from tag <table>
table1 = soup.find('table', id='main_table_countries_today')

table1


# In[6]:


# Obtain every title of columns with tag <th>

headers=[]
for i in table1.find_all('th'):
    title = i.text  
    headers.append(title)


# In[9]:


headers


# In[8]:


# convert wrapped text in column 13 into one line text
headers[13]='Test/1M pop'


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


# In[14]:


# Drop and clearing unnecessary rows
mydata.drop(mydata.index[0:7],inplace=True)
mydata.drop(mydata.index[222:229],inplace=True)
mydata.reset_index(inplace=True, drop=True)

#Drop "#" column
mydata.drop('#',inplace=True, axis=1)


# In[18]:


mydata


# In[19]:


#export to csv
mydata.to_csv('covid_data.csv', index=False)


# In[21]:


#export to csv
mydata.to_excel('covid_data.xlsx', index=False)


# In[ ]:




