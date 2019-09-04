import pandas as pd
x = 18
y = 19
while True:
    x = x - 1
    y = y - 1
    x = str(x).zfill(2)
    y = str(y).zfill(2)
    df = pd.read_csv('/home/arshreality/Desktop/EPL_Data/epl/Datasets/Full_team_matches_data/season-{0}{1}_csv.csv'.format(x,y))
    df = df[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']]

    df['HomeResult'] = 0
    df['AwayResult'] = 0
    df.loc[df['FTR'] == 'H','HomeResult'] = 1
    df.loc[df['FTR'] == 'A','HomeResult'] = 0
    df.loc[df['FTR'] == 'D','HomeResult'] = 0.5
    df.loc[df['FTR'] == 'H','AwayResult'] = 0
    df.loc[df['FTR'] == 'A','AwayResult'] = 1
    df.loc[df['FTR'] == 'D','AwayResult'] = 0.5
    df.drop(columns = 'FTR', inplace = True)

    df['scoredhome'] = df.groupby('HomeTeam')['FTHG'].cumsum()
    df['scoredaway'] = df.groupby('AwayTeam')['FTAG'].cumsum()
    df['concededhome'] = df.groupby('HomeTeam')['FTAG'].cumsum()
    df['concededaway'] = df.groupby('AwayTeam')['FTHG'].cumsum()
    df['winshome'] = df.groupby('HomeTeam')['HomeResult'].cumsum()
    df['winsaway'] = df.groupby('AwayTeam')['AwayResult'].cumsum()

    df.to_csv('/home/arshreality/Desktop/EPL_Data/epl/Datasets/ML_vars/{0}{1}.csv'.format(x,y), sep=',', encoding='utf-8')
    x = int(x)
    y = int(y)
    print(x,y)
    if x == 0:
        break
