from numpy import array


from sklearn.model_selection import KFold


# sampling the data
data = array([0.10, 0.22, 0.31, 0.43, 0.52, 0.63,0.72,0.85,0.92,0.99])

# Splittinf the data
kfold = KFold(3, True, 1)

# enumerating the splits
for train, test in kfold.split(data):
    print('train: %s, test: %s' % (data[train], data[test]))
