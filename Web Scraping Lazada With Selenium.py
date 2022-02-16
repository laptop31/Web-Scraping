import pandas as pd
import requests 
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# generating url for product

def get_url(product):
    product = product.replace(' ','+')
    template = 'https://www.lazada.com.my/catalog/?q={}'
    url = template.format(product)
    return url

def get_all_products(card):
    product_image = card.find('img')
    product_image = product_image['src']
    product_name = card.find('div','RfADt').text.strip()
    product_name = product_name.encode('ascii','ignore')
    product_name = str(product_name,'utf-8')
    product_price = card.find('div','aBrP0').text.strip()
    anchor_tag = card.a.get('href')
    product_buy_link = 'https://lazada.com.my/' + anchor_tag
    
    #pImg = card.find('img',)
    #product_image = pImg('src')
    #product_name = card.find('div','_10Wbs- _2STCsK _3IqNCf').text.strip()
    #product_price = card.find('div', 'zp9xm9 kNGSLn l-u0xK').text.strip()
    #anchor_tag = card.a.get('href')
    #product_buy_link = 'https://shopee.com.my/' + anchor_tag
    
    product_info = (product_image,product_name,product_price,product_buy_link)
    
    ############################################################################################################################################################
    
    product = input("Enter Product You're Looking For:")
    main(product)
    
    return product_info
    
def main(product):
    records = []
    url = get_url(product)
    
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get(url)
    driver.maximize_window()
    # wait for 5 sec
    time.sleep(5)
    #Define an initial value
    temp_height=0
 
    while True:
        #Looping down the scroll bar
        driver.execute_script("window.scrollBy(0,1000)")
        #sleep and let the scroll bar react
        time.sleep(5)
        #Get the distance of the current scroll bar from the top
        check_height = driver.execute_script("return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
        #If the two are equal to the end
        if check_height==temp_height:
            break
        temp_height=check_height
    
    time.sleep(10)
   

    # create a BeautifulSoup object
    soup = BeautifulSoup(driver.page_source,'html.parser')
    product_cards = soup.find_all('div','Bm3ON')
    
    for everyCard in product_cards:
        productDetails = get_all_products(everyCard)
        records.append(productDetails)
        
    # Here we are using pandas dataframe to save all the jobs information
    # in a CSV file
    
    col = ['Product_Image','Product_Name','Product Price','Product_Buy_Link']
    
    Shopee_data = pd.DataFrame(records, columns=col)
    
    Shopee_data.to_csv('C:\\Users\\USER\\Desktop\\Pandit\\Training\\LazadaData.csv')
        
product = input("Enter Product You're Looking For:")
main(product)
