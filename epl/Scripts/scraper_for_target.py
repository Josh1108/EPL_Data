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

driver = webdriver.Chrome()
URL = 'https://www.premierleague.com/stats/top/clubs/ontarget_scoring_att?se=210'
driver.get(URL)
time.sleep(10)

# here we have all the links we are required to use for a
# Particular year
d ={}
x =driver.find_elements_by_class_name('playerName')
y = driver.find_elements_by_class_name('mainStat')
for i in range(len(x)):
    d[str(x[i].text)]=str(y[i+1].text)
Year_frame =pd.DataFrame(d,index=[index_name(URL)])
Year_frame

Year_frame.to_csv('/home/arshreality/Desktop/EPL_Data/epl/Datasets/new/test18.csv')
