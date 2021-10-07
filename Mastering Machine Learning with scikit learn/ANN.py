from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

Y = [0,1,1,0]*2000
X = [[0,0],[0,1],[1,0],[1,1]]*2000
X_train, x_test, y_train, y_test = train_test_split(X,Y, random_state= 4)

clf = MLPClassifier(  hidden_layer_sizes = [2], activation = 'logistic',solver='lbfgs', random_state=4)
clf.fit(X_train,y_train)

print('number of hidden layers %s number of outputs %s', clf.n_layers_, clf.n_outputs_)
predictions = clf.predict(x_test)
print('Accuracy', clf.score(x_test, y_test))
for i, p in enumerate(predictions[:20]):
    print('the true %s  and predicted %s' %(y_test[i], p))


