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
""" zip()
for weights in ['uniform']:
    clf = neighbors.KNeighborsClassifier(3)
    clf.fit(points['Ontario'], list(range(162)))
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min = min(points['Ontario'])
    x_max = max(points['Ontario'])
    y_min = min(points['Ontario'])
    y_max = max(points['Ontario'])
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
    # Plot also the training points
    plt.scatter(points['Ontario'][0][:, 0], points['Ontario'][0][:, 1], c=y, cmap=cmap_bold)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s')"
              % (n_neighbors, weights))
"""