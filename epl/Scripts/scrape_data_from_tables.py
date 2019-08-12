import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
result = requests.get("https://www.msn.com/en-us/sports/soccer/premier-league/team-stats")

src = result.content

soup = BeautifulSoup(src, 'lxml')
table = soup.table
table_rows = table.find_all('tr', class_ = 'rowlink')
iterations = iter(table_rows)
# next(iterations)
team_names = []
total_shots = []
total_on_target = []
for tr in iterations:
    td = tr.find_all('td')
    row = [i.text for i in td]
    team_names.append(row[2])
    total_shots.append(row[6])
    total_on_target.append(row[7])

print(team_names)
print(total_shots)
print(total_on_target)

df = pd.DataFrame(list(zip(team_names, total_shots, total_on_target)))
print(df)

df.to_csv('1819.csv', sep=',', encoding='utf-8',index = False)

# for link in links:
#     if "mainStat" in link.attrs:
#         print(link)
        # print(link.attrs['href'])
