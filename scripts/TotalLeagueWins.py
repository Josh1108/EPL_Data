# libraries
import numpy as np
import pandas as pd
import csv
import cv2
import matplotlib.pyplot as plt
from matplotlib import rc
import scipy
from imageio import imread

def connectpoints(x1,y1,x2,y2):
    plt.plot([x1,x2],[y1,y2],'-')

def image_plot(counts, images, spacing=0, X_label='x', Y_label='y',Title = 'Title'):
    # Iterate through images and data, autoscaling the width to
    # the aspect ratio of the image
    height = 2
    for i, (count, img) in enumerate(zip(counts, images)):
        AR = img.shape[1] / img.shape[0]
        width = height
        left = width*i + spacing*i
        right = left + width
        for j in range(count):
            plt.imshow(img, extent=[left, right, height*j, height*(j+1)])
        plt.text((left + right - 0.7) / 2 , height*count + 0.5, list_of_winners[i],fontsize = 15, rotation = 90)

    # Set size of figure
    plt.rcParams["figure.figsize"] = (25,25)

    # set font
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Helvetica'

    # set the style of the axes and the text color
    plt.rcParams['axes.edgecolor']='#333F4B'
    plt.rcParams['axes.linewidth']=0.8
    plt.rcParams['xtick.color']='#333F4B'
    plt.rcParams['ytick.color']='#333F4B'
    plt.rcParams['text.color']='#333F4B'

    # Set x,y limits and labels on plot window
    plt.xlim(0, right)
    plt.ylim(0, max(counts)*2)
    plt.xticks(np.arange(1,108,108/len(years)), years, rotation = 90)
    plt.yticks(np.arange(1,32.5,2.2), range(1,14))
    plt.tick_params(axis='both', length = 0)
    plt.xlabel(X_label)
    plt.ylabel(Y_label)
    plt.title(Title)
    plt.savefig('ass.png', dpi=300, bbox_inches='tight')

# Importing Table Req to create graph
df = pd.read_csv('scripts/Seasonresults/winners.csv')

# Assign label names for plotting
X_label1 = 'Years'
Y_label1 = 'Premier League Wins'
Title1 = 'Total Premier League Wins by Team and Year'
path = 'scripts/logos'
# Read in logo images and set them to equal sqaures
man_united_logo = cv2.resize(imread(path + '/mu.png'), (400, 400))
man_city_logo = cv2.resize(imread(path +'/mc.png'), (400, 400))
chelsea_logo = cv2.resize(imread(path +'/c.png'), (400, 400))
arsenal_logo = cv2.resize(imread(path +'/a.png'), (400, 400))
leicester_logo = cv2.resize(imread(path +'/lc.png'), (400, 400))
blackburn_logo = cv2.resize(imread(path +'/br.png'), (400, 400))

# Convert each column of dataframe to lists for plotting
count = df['Count'].tolist()
list_of_winners = df['Winner'].tolist()
years = df['Year'].tolist()

# Creating a list of logos
logos = [man_united_logo,man_united_logo,blackburn_logo,man_united_logo,man_united_logo,arsenal_logo,man_united_logo,man_united_logo,man_united_logo,arsenal_logo,man_united_logo,arsenal_logo,chelsea_logo,chelsea_logo,man_united_logo,man_united_logo,man_united_logo,chelsea_logo,man_united_logo,man_city_logo,man_united_logo,man_city_logo,chelsea_logo,leicester_logo,chelsea_logo,man_city_logo,man_city_logo]

image_plot(count, logos, spacing = 2, X_label = X_label1, Y_label = Y_label1, Title = Title1)
