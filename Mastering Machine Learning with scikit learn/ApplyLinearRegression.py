import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import cross_val_score,train_test_split

df = pd.read_csv('winequality-red.csv', sep = ';')
print(df.describe())
X = df[list(df.columns)[:-1]]
y = df['quality']
print(df.describe())
X_train,y_train, x_test, y_test =train_test_split(X, y)

regressor = LinearRegression()

##scores  = cross_val_score(regressor, X,y, cv=5)
##print(scores.mean(), scores)

regressor.fit(X_train,y_train)
predictions = regressor.predict(x_test)
for i, prediction in enumerate(predictions):
    print("Predicted:%s, True %s",prediction, y_test[i])
##
##plt.figure()
##plt.scatter(df['alcohol'], df['quality'])
##
##plt.show()
