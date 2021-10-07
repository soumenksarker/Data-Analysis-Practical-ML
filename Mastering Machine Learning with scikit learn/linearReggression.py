import pandas as pd
import quandl
df = quandl.get("WIKI/GOOG")
print(df.head())
df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
print(df.head())

import quandl,math
import numpy as np
from sklearn import preprocessing, svm, cross_validation
from sklearn.linear_model import LinearRegression
forcast_col = 'Adj. Close'
df.fillna(value= -9999, inplace = True)
forecast_out = int(math.ceil(.01*len(df)))
df['label'] = df[forcast_col].shift(-forecast_out)
#print(df.head())
X = df.dropna(inplace = True)
X = np.array(df.drop(['label'], 1))
y = np.array(df['label'])
X = preprocessing.scale(X)
y = np.array(df['label'])
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=.20)
clf = svm.SVR()
clf.fit(X_train, y_train)
accureccy = clf.score(X_test, y_test)
print(accureccy)
