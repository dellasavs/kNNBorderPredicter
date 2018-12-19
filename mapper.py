import tensorflow as tf
from tensorflow import keras
from sklearn import neighbors
from matplotlib.colors import ListedColormap
import numpy as np
import math
import matplotlib.pyplot as plt

placeLabel =   {'Ontario': 0,
                'Michigan': 1,
                'Quebec': 2,
                'NY': 3,
                'Manitoba': 4,
                'Wisconsin': 5,
                'Ohio': 6,
                'Minnesota': 7}

places = ['Ontario', 'Quebec', 'NY', 'Michigan', 'Manitoba', 'Wisconsin', 'Ohio', 'Minnesota']
labels = []
allPoints = []
pointCount = 400
classCount = 8

def init(places):
        for place in places:
                f=open(place + 'Pulled.txt', 'r')
                for i in range(pointCount):
                        coord = f.readline().split(',')
                        labels.append(placeLabel[place])
                        allPoints.append([float(coord[1])*-1,float(coord[0])])

init(places)
k = 5 # nearest neighbours
h = .02  # step size in the mesh

#Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF', '#FFFFAF', '#FF9EE1', '#d6d6d6', '#ADFFFA', '#f9bd6d'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00B2', '#7c7c7c', '#00FFFA', '#f98d00'])

for weights in ['uniform']:
    clf = neighbors.KNeighborsClassifier(n_neighbors=k)
    clf.fit(allPoints, labels)
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min = min(p[0] for p in allPoints)
    x_max = max(p[0] for p in allPoints)
    y_min = min(p[1] for p in allPoints)
    y_max = max(p[1] for p in allPoints)
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    print('Predicting borders')
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    print('Borders predicted')
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
    # Plot also the training points
    plt.scatter(list(p[0] for p in allPoints), list(p[1] for p in allPoints), c=labels, cmap=cmap_bold)
    plt.axis([100, 60, 40, 60])
    plt.title("N-Class classification (k = %i, total training points = '%s')"
              % (k, pointCount*classCount))
plt.show()