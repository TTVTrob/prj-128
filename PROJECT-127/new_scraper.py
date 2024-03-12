from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests
import pandas as pd
START_URL="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(START_URL)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find_all('table', {'class' : 'wikitable sortable jquery-tablesorter'})
data=[]
new=table[1].find_all("tr")
for tr in new:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    data.append(row)
name=[]
distance=[]
radius=[]
mass=[]
for i in range(1,len(data)):
    name.append(data[i][0])
    distance.append(data[i][5])
    mass.append(data[i][7])
    radius.append(data[i][6])
header=["star_name","distance","mass","radius"]
df=pd.DataFrame(list(zip(name,distance,mass,radius)),columns=header)
df.to_csv("df.csv",index=True,index_label="id")
