import pandas as pd
df = pd.read_csv(
    '../epl/datasets/EPLStandings.csv', index_col=0).T

# print(df_stats.sort_values('punches').fillna(0))
# print(list(df_stats.loc[ 'Manchester United' , : ]))
# print(df_stats.corr())
# print(df_stats)
# print(len(df[df['FTR']=='D']['FTR']))
# print(list(range(2001,2019)))

print(df['Arsenal'].min())

# print(list(df.columns))
print(df[df['Arsenal'] == df['Arsenal'].min()].index[0]) 