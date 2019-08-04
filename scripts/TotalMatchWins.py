# libraries
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.patches as mpatches

path = 'scripts/Seasonresults/EPL_Set.csv'
EPL_set =pd.read_csv(path)

List_of_teams = set(EPL_set['HomeTeam'].values)
dic_of_wins= {el:0 for el in List_of_teams}
dic_of_wins # Created a dictionary of teams and their wins. Now we'll take the wins from table and as we
            # Traverse through it we'll update it here
dic_of_losses={el:0 for el in List_of_teams}
dic_of_draws={el:0 for el in List_of_teams}

# Updating dictionary as per wins losses and draws
with open(path,'r') as file:
  data =csv.reader(file)
  header= next(data)
  for row in data:
    if row[6]=='A' :
      dic_of_wins[str(row[3])]+=1
      dic_of_losses[str(row[2])]+=1
    elif row[6]=='H' :
      dic_of_wins[str(row[2])]+=1
      dic_of_losses[str(row[3])]+=1
    else:
      dic_of_draws[str(row[2])]+=1
      dic_of_draws[str(row[3])]+=1
dic_of_draws.items()


# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Helvetica'

# set the style of the axes and the text color
plt.rcParams['axes.edgecolor']='#333F4B'
plt.rcParams['axes.linewidth']=0.8
plt.rcParams['xtick.color']='#333F4B'
plt.rcParams['ytick.color']='#333F4B'
plt.rcParams['text.color']='#333F4B'

mydicts = [dic_of_draws,dic_of_wins, dic_of_losses]
df = pd.concat([pd.Series(d) for d in mydicts], axis=1).fillna(0)
df.reset_index(inplace =True)
list(df[0].values)
df.columns=['Name','draws','wins','losses']
list(df['wins'].values)

df['Total']= df['wins']+df['draws'] + df['losses']
df
df.sort_values(by=['Total','wins'],ascending = True,inplace =True)
df.reset_index(inplace =True)
df.drop('index',inplace =True,axis=1)

# we first need a numeric placeholder for the y axis
my_range=list(range(1,len(df.index)+1))
my_range
fig, ax = plt.subplots(figsize=(10,15))

# create for each expense type an horizontal line that starts at x = 0 with the length
# represented by the specific expense percentage value.
plt.hlines(y=my_range, xmin=0, xmax=df['wins'], color='#00ccb8', alpha=0.4, linewidth=6)
plt.hlines(y=my_range, xmin=df['wins'], xmax=df['wins']+df['draws'], color='#007ACC', alpha=0.4, linewidth=6)
plt.hlines(y=my_range, xmin=df['wins']+df['draws'], xmax=df['wins']+df['draws']+df['losses'], color='#0014cc', alpha=0.4, linewidth=6)


wins_label = mpatches.Patch(color='#00ccb8', label='wins')
draws_label = mpatches.Patch(color='#007ACC', label='draws')
loss_label = mpatches.Patch(color='#0014cc', label='losses')
ax.legend(handles=[wins_label,draws_label,loss_label],loc =7)


# create for each expense type a dot at the level of the expense percentage value
plt.plot(df['wins'], my_range, "o", markersize=6, color='#00ccb8', alpha=0.8)
plt.plot(df['wins']+df['draws'], my_range, "o", markersize=6, color='#007ACC', alpha=0.8)
plt.plot(df['wins']+df['draws']+df['losses'], my_range, "o", markersize=6, color='#0014cc', alpha=0.8)

# set labels
ax.set_xlabel('Number of Wins, Losses & Draws', fontsize=15, fontweight='black', color = '#333F4B')
ax.set_ylabel('')
# set axis
ax.tick_params(axis='both', which='major', labelsize=12)
plt.yticks(my_range, df['Name'])
plt.title('Wins, Losses & Draws for each team')

# change the style of the axis spines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)
plt.axvline(x=200,ymax = 0.96,color = 'black',linewidth = 0.5, alpha =0.5)
plt.axvline(x=400,ymax = 0.96,color = 'black',linewidth = 0.5, alpha =0.5)
plt.axvline(x= 600,ymax = 0.96,color = 'black',linewidth = 0.5, alpha =0.5)
plt.axvline(x= 800,ymax = 0.96,color = 'black',linewidth = 0.5, alpha =0.5)
# set the spines position
ax.spines['bottom'].set_position(('axes', 0))
ax.spines['left'].set_position(('axes', 0.015))
# plt.savefig('hist2.png', dpi=300, bbox_inches='tight')
