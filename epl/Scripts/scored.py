import pandas as pd
# x = 19
# while True:
# y = 20
#     x = x - 1
#     y = y - 1
#     x = str(x).zfill(2)
#     y = str(y).zfill(2)
df = pd.read_csv('/home/arshreality/Desktop/EPL_Data/epl/Datasets/E0.csv',index_col=0)
df.head()
for team in df['HomeTeam'].unique():
    print(team, df.loc[df['HomeTeam'] == team, 'FTHG'].sum() + df.loc[df['AwayTeam'] == team, 'FTAG'].sum())

df['scoredhome'] = df.groupby('HomeTeam')['FTHG'].cumsum()
df['scoredaway'] = df.groupby('AwayTeam')['FTAG'].cumsum()
df['concededhome'] = df.groupby('HomeTeam')['FTAG'].cumsum()
df['concededaway'] = df.groupby('AwayTeam')['FTHG'].cumsum()
df['winshome'] = df.groupby('HomeTeam')['HomeResult'].cumsum()
df['winsaway'] = df.groupby('AwayTeam')['AwayResult'].cumsum()
df

df = df[::-1]
df.to_csv('/home/arshreality/Desktop/EPL_Data/epl/Datasets/E0.csv', sep=',', encoding='utf-8',index_label = 'team', index = True)
    # x = int(x)
    # y = int(y)
    # print(x,y)
    # if x == 7:
    #     break
