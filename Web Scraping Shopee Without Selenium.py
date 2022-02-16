# Web_Scrapping_For_Shopee

import pandas as pd
import requests
from bs4 import BeautifulSoup

# generate url for product

def get_url(product_name):
    product_name = product_name.replace(' ','%20')
    product_name = product_name.replace("'s",'%27')
    template = 'https://shopee.com.my/search?keyword={}'
    url = template.format(product_name)
    return url

url = get_url('cat')
print(url)

# Check respone

response = requests.get(url)
print(response)

# Create BeautifulSoup Object

soup = BeautifulSoup(response.text,'html.parser')

# Here we are searching for all div tag having class name col-xs-2-4

cards= soup.find_all('div','col-xs-2-4')
print(len(cards))
