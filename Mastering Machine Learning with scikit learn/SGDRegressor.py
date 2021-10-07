import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import SGDRegressor
from sklearn.cross_validation  import cross_val_score,train_test_split
from sklearn.preprocessing import scale
data = load_boston()



X_train,x_test,y_train,y_test = train_test_split(data.data, data.target)
X_train = scale(X_train)
y_train = scale(y_train)

x_test = scale(x_test)

y_test = scale(y_test)
regressor = SGDRegressor(loss='squared_loss')
scores = cross_val_score(regressor, X_train, y_train, cv=7)

print ('Cross validation r-squared scores:', scores)
print ('Average cross validation r-squared score:', np.mean(scores))
regressor.fit(X_train, y_train)
print ('Test set r-squared score', regressor.score(x_test, y_test))
