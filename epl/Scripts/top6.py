import pandas as pd
x = 19
y = 20
while True:
    x = x - 1
    y = y - 1
    x= str(x).zfill(2)
    y = str(y).zfill(2)
    df = pd.read_csv('/home/arshreality/Desktop/EPL_Data/epl/Datasets/Transposed shot accuracy/{0}{1}new.csv'.format(x,y),index_col=0)
    df = df[['Arsenal','Chelsea','Everton','Liverpool','Manchester United','Tottenham Hotspur']]
    df = df.rename_axis(None)
    df.rename(index = {"shot_acc": "20{0}-{1}".format(x,y),}, inplace = True)
    df.to_csv('/home/arshreality/Desktop/EPL_Data/epl/Datasets/Transposed shot accuracy top 6/{0}{1}newnew.csv'.format(x,y), sep=',', encoding='utf-8',index_label = 'team', index = True)
    x = int(x)
    y = int(y)
    if x == 0:
        break
