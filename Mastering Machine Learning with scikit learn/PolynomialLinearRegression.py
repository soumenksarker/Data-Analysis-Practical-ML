import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X_train = [[6], [8], [10], [14], [18]]
y_train = [[7], [9], [13], [17.5], [18]]
X_test = [[6], [8], [11], [16]]
y_test = [[8], [12], [15], [18]]

regressor = LinearRegression()
regressor.fit(X_train, y_train)
xx = np.linspace(0,26,100)
yy = regressor.predict(xx.reshape(xx.shape[0], 1))

quadratic_featurizer = PolynomialFeatures(degree =2)
X_train_quadratic = quadratic_featurizer.fit_transform(X_train)
X_test_quadratic = quadratic_featurizer.fit_transform(X_test)

regressor_quadratic = LinearRegression()
regressor_quadratic.fit(X_train_quadratic, y_train)
xx_quadratic = quadratic_featurizer.transform(xx.reshape(xx.shape[0],1))
plt.plot(xx, regressor_quadratic.predict(xx_quadratic), c='r', linestyle = '--')

print(X_train)
print(X_train_quadratic)
print(X_test)
print(X_test_quadratic)
print("Simpler linear_regression r-square",regressor.score(X_test, y_test))
print("Quadratice linear regression r-square",regressor_quadratic.score(X_test_quadratic, y_test))

plt.title("Pizza price regressed on diameter")
plt.xlabel("Diameter in inches")
plt.ylabel("Price in Doller")
plt.axis([0,25,0,25])
plt.grid(True)
plt.scatter(X_train, y_train)
plt.plot(xx,yy)
plt.show()
