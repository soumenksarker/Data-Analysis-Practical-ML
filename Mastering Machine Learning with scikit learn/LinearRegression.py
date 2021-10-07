import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
X = [[6],[8],[10],[14],[18]]
Y = [[7],[9],[13],[17.5],[18]]
X_test = [[8], [9], [11], [16], [12]]
y_test = [[11], [8.5], [15], [18], [11]]
model = LinearRegression()
model.fit(X,Y)
print (model.predict([12]))
print ("R-squared:%.4f" %model.score(X_test, y_test))
plt.figure()
plt.title("Pizza price plotted against diameter")
plt.xlabel("Diameter in inches")
plt.ylabel("Price in dollers")
plt.scatter(X,Y)
plt.axis([0,25,0,25])
plt.grid(True)
plt.show()

