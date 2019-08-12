import matplotlib as mpl
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import seaborn as sns
mpl.style.use('ggplot') # optional: for ggplot-like style
import pandas as pd
import glob

path = r'/home/arshreality/Desktop/epl/Datasets/Transposed shot accuracy top 6' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
frame.sort_values(by=['team'], inplace = True)
frame.head()

# Make the plot

parallel_coordinates(frame, 'team',sort_labels = True)
plt.xticks(rotation = 90)
plt.ylabel('Shot Accouracy %')
plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")
fig1 = plt.gcf()
plt.title('Shot accuracy for six teams to never get relegated from 2000-2019')
plt.show()
plt.draw()

fig1.savefig('/home/arshreality/Desktop/epl/Images/shot_acc_for_test.png', dpi=300,bbox_inches = 'tight')
# plt.savefig('/home/arshreality/Desktop/epl/Images/shot_acc_for_20{0}-{1}.png'.format(x,y), dpi=300, bbox_inches='tight')
