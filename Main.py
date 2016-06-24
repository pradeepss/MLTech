import matplotlib.mlab as mlab
import numpy as np
import sklearn
import matplotlib.pyplot as plt #plot the data
from sklearn import datasets    #organizes data for us
from sklearn import svm     #provides simple vector machine learning framework to interpret the data
import random
import math
from scipy.stats import norm



# digits = datasets.load_digits()
#
# # print(digits.data)
# # print(digits.target)
# # print(digits.images[0])
#
# clf = svm.SVC(gamma=0.001,C=100)    #classifier gamma more closer to zero will get you higher probability but will slow to run
#
# # print(len(digits.data))
#
# x,y = digits.data[:-10], digits.target[:-10]
#
# clf.fit(x,y)
# # print('Prediction: ',clf.predict(digits.`)
# plt.imshow(digits.images[-10],cmap=plt.cm.gray_r,interpolation="nearest")
# plt.show()


#generate 10000 random variables and store it in a data set
gausian = []
seq = []

for i in range(10000):
    gausian.append(random.randint(1, 10))
    seq.append(i)


me = np.mean(gausian[1:])
med = np.median(gausian[1:])
s = np.std(gausian[1:])
mn = np.min(gausian[1:])
mx = np.max(gausian[1:])

variance = np.square(s)

print me,med,s,variance,mn,mx
# mu = math.
# variance = 1
# sigma = math.sqrt(variance)
# x = np.linspace(-3, 3, 100)
# plt.plot(x,mlab.normpdf(x, mu, sigma))
#
# plt.show()



# Plot between -10 and 10 with .001 steps.
x_axis = np.arange(mn-2, mx+2, 0.001)
# Mean = 0, SD = 2.
# plt.plot(x_axis, norm.pdf(x_axis,me,s))
plt.plot(seq[1:],gausian[1:],'*')
plt.axis([mn, mx, 0, 10])
plt.show()
