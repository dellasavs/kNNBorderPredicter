import tensorflow as tf
from tensorflow import keras
from sklearn import neighbors
import numpy as np
import math
import matplotlib.pyplot as plt

def pull(place, l):
    l.append([])
    l.append([])
    f=open(place + 'Pulled.txt', 'r')
    for i in range(162):
        coord = f.readline().split(',')
        coord[0] = coord[0].replace("(", "")
        coord[1] = coord[1].replace(")", "")
        l[0].append(float(coord[0]))
        l[1].append(float(coord[1])*-1)

places = ['Ontario', 'Quebec', 'NY', 'Michigan', 'Manitoba', 'Wisconsin', 'Ohio', 'Minnesota']
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'cyan', 'black', 'green']
marker = 'o'
points = {}
zipper = []

def init(places):

    for place in places:
        points[place] = []
        pull(place, points[place])
        #points[place] = list(zip(zipper[0], zipper[1]))

    i=0
    for place in places:
        plt.plot(points[place][1], points[place][0], color=str(colors[i]), marker=str(marker), lineStyle='')
        i=i+1

init(places)
plt.axis([100, 60, 40, 60])
plt.show()