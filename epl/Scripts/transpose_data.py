import pandas as pd
x = 19
y = 20
while True:
    x = x - 1
    y = y - 1
    x= str(x).zfill(2)
    y = str(y).zfill(2)
    df = pd.read_csv('/home/arshreality/Desktop/EPL_Data/epl/Datasets/Shots and shot on target/{0}{1}.csv'.format(x,y))
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

    df_new.to_csv('/home/arshreality/Desktop/EPL_Data/epl/Datasets/Transposed shot accuracy/{0}{1}new.csv'.format(x,y), sep=',', encoding='utf-8',index_label = 'team', index = True)
    x = int(x)
    y = int(y)
    print(x,y)
    if x == 0:
        break
