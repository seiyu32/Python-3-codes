import dataset
import matplotlib.pyplot as plt
import the as the
from sklearn import datasets
from sklearn import svm
from sklearn.svm._libsvm import predict

digits = datasets.load_digits() // dataset
clf = svm.SVC(gamma=0.001, C=100)
print(len(digits.data))
x, y = digits.data[:-1], digits.target[:-1] // train
the
data
clf.fit(x, y)
print('Prediction:', clf.predict(digits.data[-1])) // predict
the
data
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()