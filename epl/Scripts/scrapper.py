# A function
def index_name(s):
    count =0
    t=''
    for ch in s:
        if ch=='/' and count!=6:
            count+=1
        elif ch == '?' and count ==6:
            break
        elif count==6:
            t+=ch
    return t

# Importing Libraries

import pandas as pd
import time
from selenium import webdriver

driver = webdriver.Firefox()
URL = 'https://www.premierleague.com/stats/top/clubs/wins?se=16'
driver.get(URL)
time.sleep(10)
list_of_features=[]
elem = driver.find_elements_by_class_name('topStatsLink')
for elems in elem:
    list_of_features.append(elems.get_attribute('href'))

# here we have all the links we are required to use for a
# Particular year
d ={}
x =driver.find_elements_by_class_name('playerName')
y = driver.find_elements_by_class_name('mainStat')
for i in range(len(x)):
    d[str(x[i].text)]=str(y[i+1].text)
Year_frame =pd.DataFrame(d,index=[index_name(URL)])
Year_frame

for link in list_of_features:
    if link ==URL:
        continue
    dict_temp={}
    driver.get(link)
    time.sleep(10)
    x =driver.find_elements_by_class_name('playerName')
    y = driver.find_elements_by_class_name('mainStat')
    for i in range(len(x)):
        dict_temp[str(x[i].text)]=str(y[i+1].text)
    Year_frame_temp=pd.DataFrame(dict_temp,index=[index_name(link)])
    Year_frame=pd.concat([Year_frame_temp,Year_frame],sort=False)
Year_frame
Year_frame.to_csv('/home/jushaan/football/epl/Datasets/PremierLeagueOff06-19/EPL_2007.csv')
