from bs4 import BeautifulSoup 
import requests
import pandas as pd
from selenium import webdriver
import time

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"

browser = webdriver.Chrome()
browser.get(START_URL)
time.sleep(10)

soup = BeautifulSoup(browser.page_source, "html.parser")

star_table = soup.find_all('table')

temp_list= []

def scrape():
    table_rows = star_table[7].find_all('tr')

    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text.rstrip() for i in td]
        temp_list.append(row)

    Star_names = []
    Distance =[]
    Mass = []
    Radius =[]
    Luminosity =[]


    for i in range(1,len(temp_list)):
    
        Star_names.append(temp_list[i][0])
        Distance.append(temp_list[i][5])
        Mass.append(temp_list[i][7])
        Radius.append(temp_list[i][8])
        Luminosity(temp_list[i][9])

    df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
    print(df2)

    df2.to_csv('scraped_data.csv')