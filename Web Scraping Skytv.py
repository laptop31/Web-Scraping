import csv 
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd

# generating url for job position and location

def get_url():
    template = 'https://guidatv.sky.it/canali'
    url = template
    return url

# Create A Function 
# Scrape The Job Information from EveryCard

def get_channel(card):
    channel_name = card.find('h3','caption medium c-channelsCard__title').text
    anchor_tag = card.a
    channel_url = anchor_tag['href']
    channel_num = card.find('span','caption c-channelsCard__span').text
    
    channel_info = (channel_name,channel_url,channel_num)
    
    return channel_info


# create our main function

def main():
    records = []
    url = get_url()
    response = requests.get(url)
    
    # Creating BeautifulSoup Object

    soup = BeautifulSoup(response.text,'html.parser')
    # Here we are searching for div tags having
    # sx2jih0 zcydq852 zcydq842 zcydq872 zcydq862 zcydq82a zcydq832 zcydq8d2 zcydq8cq
    # class name
    cards = soup.find_all('div','c-channelsCard__container')
    
    for everyCard in cards:
        channel_details = get_channel(everyCard)
        records.append(channel_details)
    
    # Here we are using pandas dataframe to save all the jobs information
    # in a CSV file
    
    col = ['Channel_Name', 'Channel_URL', 'Channel_Num']
    
    channel_data = pd.DataFrame(records, columns=col)
    
    channel_data.to_csv('D:\\Job Seeking\\Informa Tech\\ChannelData.csv')

    ######################################################################################################################################
    main()
    