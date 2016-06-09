import matplotlib
import numpy
import sklearn
import matplotlib.pyplot as plt #plot the data
from sklearn import datasets    #organizes data for us
from sklearn import svm     #provides simple vector machine learning framework to interpret the data

digits = datasets.load_digits()

# print(digits.data)
# print(digits.target)
# print(digits.images[0])

clf = svm.SVC(gamma=0.001,C=100)    #classifier gamma more closer to zero will get you higher probability but will slow to run

# print(len(digits.data))

x,y = digits.data[:-10], digits.target[:-10]

clf.fit(x,y)
# print('Prediction: ',clf.predict(digits.`)
plt.imshow(digits.images[-10],cmap=plt.cm.gray_r,interpolation="nearest")
plt.show()