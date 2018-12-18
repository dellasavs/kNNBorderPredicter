import tensorflow as tf
from tensorflow import keras

import numpy as np
import math
import matplotlib.pyplot as plt

x= []
y= []
x1=[]
y1=[]
test_x = []
test_y = []

test_label = []
train_label= []

def pull():
    f=open('ONpoints.txt', 'r')
    for i in range(162):
        coord = f.readline().split(',')
        coord[0] = coord[0].replace("(", "")
        coord[1] = coord[1].replace(")", "")
        x.append(float(coord[0]))
        y.append(float(coord[1])*-1)
        train_label.append(1)
    f=open('otherpoints.txt', 'r')
    for i in range(171):
        coord = f.readline().split(',')
        coord[0] = coord[0].replace("(", "")
        coord[1] = coord[1].replace(")", "")
        x1.append(float(coord[0]))
        y1.append(float(coord[1])*-1)
        train_label.append(0)
    f=open('test.txt', 'r')
    for i in range(22):
        coord = f.readline().split(',')
        test_x.append(float(coord[0]))
        test_y.append(float(coord[1])*-1)
        test_label.append(float(coord[2]))

def distance(x0, y0, x1, y1):
    return math.sqrt(((x0-x1)**2 + (y0-y1)**2))

def nns(x, y, xlist, ylist):
    best = [0,0]
    bestDist = 99999
    bestIndex = -1
    i=0
    for i in range(len(xlist)):
        dist = distance(x,y,xlist[i],ylist[i])
        if(dist<bestDist):
            bestDis = dist
            best[0] = xlist[i]
            best[1] = ylist[i]
            bestIndex = i 
    print('[' + str(x) + ', ' + str(y) + ']: Closest point = (' + str(best[0])+','+str(best[1])+')')
    plt.plot(x,y, 'ro')
    plt.plot(best[0],best[1], 'bo')
    return bestIndex

pull()
x_train = x
y_train = y
correct=0
incorrect=0
i=0
for i in range(len(test_x)):
    predictedLabel = train_label[nns(test_x[i], test_y[i], x_train, y_train)]
    if(predictedLabel==test_label[i]):
        correct=correct+1
    else:
        incorrect=incorrect+1

print('Correct answers: ' + str(correct))
print('Incorrect answers: ' + str(incorrect))


#plt.plot(x1,y1, 'bo')
#plt.axis([41, 60, 70, 100])
plt.gca().invert_xaxis()
plt.show()