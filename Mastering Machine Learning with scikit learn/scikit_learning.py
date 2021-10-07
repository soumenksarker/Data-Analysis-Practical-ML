
import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from statistics import mean
style.use('fivethirtyeight')

housing_data = pd.read_pickle('HPI.pickle2')
housing_data = housing_data.pct_change()

housing_data.replace([np.inf, -np.inf], np.nan, inplace=True)
housing_data['US_HPI_future'] = housing_data['US_HPI'].shift(-1)
housing_data.dropna(inplace=True)


def create_labels(cur_hpi, fut_hpi):
    if fut_hpi > cur_hpi:
        return 1
    else:
        return 0
def moving_average(values):
    ma = mean(values)
    return ma
housing_data['label'] = list(map(create_labels,housing_data['US_HPI'], housing_data['US_HPI_future']))
#print(housing_data[['US_HPI_future' ,'US_HPI']].head())

#housing_data['ma_apply_example'] = pd.rolling_apply(housing_data['M30'], 10, moving_average)
#print(housing_data.tail())

from sklearn import svm, preprocessing, cross_validation

X = np.array(housing_data.drop(['label','US_HPI_future'], 1))

X = preprocessing.scale(X)
print(X)
y = np.array(housing_data['label'])
print(y)
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2 )
clf = svm.SVC(kernel = 'linear')
print(clf)
clf.fit(X_train, y_train)
#
#pred = predict(X_test)
print(clf.score(X_test, y_test))
