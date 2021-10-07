from os import walk, path
import numpy as np
import mahotas as mh
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

X=[]
y=[]
for dir_path, dir_names, file_names in walk('data/att-faces/orl_faces'):
    for fn in file_names:
        if (fn[-3:] == 'pgm'):
           image_filename = path.join(dir_path, fn)
           X.append(scale(mh.imread(image_filename, as_grey=True).reshape(10304).astype('float32')))
           y.append(dir_path)

X=np.array(X)

x_train,x_test,y_train,y_test = train_test_split(X,y)
pca=PCA(n_components=150)

x_train_reduced = pca.fit_transform(x_train)
x_test_reduced = pca.transform(x_test)

print('The original dimensions of the training data were', x_train.shape)
print('The reduced dimensions of the training data were', x_train_reduced.shape)
classifier = LogisticRegression()
accuracies = cross_val_score(classifier, x_train_reduced, y_train)
print('Cross validaion accuracy:', np.mean(accuracies),accuracies)
classifier.fit(x_train_reduced, y_train)
predictions = classifier.predict(x_test_reduced)
print(classification_report(y_test, predictions))
