import pandas as pd

df = pd.read_csv('/home/arshreality/Desktop/epl/season-0001_csv.csv')
df.columns

df = df[['HomeTeam', 'AwayTeam','HS', 'AS', 'HST', 'AST']]
df_new = pd.DataFrame()

df_new['team'] = sorted(list(set(df['HomeTeam'].tolist())), reverse = False)
df_new
HS_list = []
AS_list = []
HST_list = []
AST_list = []

for i in df_new['team'].tolist():
    HS_list.append(df.loc[df['HomeTeam'] == i, 'HS'].sum())
for i in df_new['team'].tolist():
    AS_list.append(df.loc[df['AwayTeam'] == i, 'AS'].sum())
for i in df_new['team'].tolist():
    HST_list.append(df.loc[df['HomeTeam'] == i, 'HST'].sum())
for i in df_new['team'].tolist():
    AST_list.append(df.loc[df['AwayTeam'] == i, 'AST'].sum())
HS_list
AS_list
HST_list
AST_list

total_shots_list = []
total_on_target_list = []
for (i,j,k,l) in zip(HS_list,AS_list,HST_list,AST_list):
    total_shots_list.append(i + j)
    total_on_target_list.append(k+l)

total_shots_list
total_on_target_list

shot_acc_list = []
for (i,j) in zip(total_shots_list,total_on_target_list):
    shot_acc_list.append((j/i)*100)

df_new['total_shots'] = total_shots_list
df_new['total_on_target'] = total_on_target_list
df_new['shot_acc'] = shot_acc_list

df_new

df_new.to_csv('0001.csv', sep=',', encoding='utf-8',index = False)
