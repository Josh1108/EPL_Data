import pandas as pd
df = pd.read_csv('/home/arshreality/Desktop/epl/Datasets/Shots and shot on target/0102.csv')
df.columns
df = df[['team','shot_acc']]

df_new = df.T
df_new
new_header = df_new.iloc[0] #grab the first row for the header
df_new = df_new[1:] #take the data less the header row
df_new.columns = new_header #set the header row as the df header

df_new

# as_list = df_new.index.tolist()
# as_list[0] = 'shot_acc'
# df_new.index = as_list

df_new

df_new.to_csv('/home/arshreality/Desktop/epl/Datasets/Transposed shot accuracy/0102new.csv', sep=',', encoding='utf-8',index_label = 'team', index = True)
