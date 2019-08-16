import pandas as pd # primary data structure library
import matplotlib as mpl
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import seaborn as sns
mpl.style.use('ggplot') # optional: for ggplot-like style
x = 19
y = 20
while True:
    x = x - 1
    y = y - 1
    x= str(x).zfill(2)
    y = str(y).zfill(2)
    df = pd.read_csv('/home/arshreality/Desktop/EPL_Data/epl/Datasets/Transposed shot accuracy/{0}{1}new.csv'.format(x,y))

    # Make the plot
    parallel_coordinates(df, 'team', colormap=plt.get_cmap("Set2"))
    plt.xticks(rotation = 90)
    plt.ylabel("Shot Accuracy %")
    plt.title('Shot accuracy for every team in 20{0}-{1}'.format(x,y))
    fig1 = plt.gcf()
    plt.show()
    fig1.savefig('/home/arshreality/Desktop/EPL_Data/epl/Images/shot_acc_for_20{0}-{1}.png'.format(x,y), dpi=300, bbox_inches='tight')
    x = int(x)
    y = int(y)
    if x == 7:
        break
