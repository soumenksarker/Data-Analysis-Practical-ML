import numpy as np
import mahotas as mh
from mahotas.features import surf
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import*
from sklearn.cluster import MiniBatchKMeans
import glob #globing of directory module contains os,sys,re

all_instance_filenames = []
all_instance_targets = []
for f in glob.glob('New folder/*.jpg'):
    if('cat' in f):  ## make cat are positve class and dogs are negative
        target=1
    else:
        target=0
        
    all_instance_filenames.append(f)
    all_instance_targets.append(target)

print(all_instance_targets)
surf_features = []
counter =0
for f in all_instance_filenames: ##Extract all surf descriptors from all of images
    print('Reading image:', f)
    image = mh.imread(f, as_grey=True)
    surf_features.append(surf.surf(image)[:, 5:]) 
    
train_len = int(len(all_instance_filenames) * .60)##60% are training instances
X_train_surf_features = np.concatenate(surf_features[:train_len])
x_test_surf_features = np.concatenate(surf_features[train_len:])
y_train = all_instance_targets[:train_len]
y_test = all_instance_targets[train_len:]

n_clusters = 300;
print('Clustering', len(X_train_surf_features),'features')##made 300 cluster from train Surf features
estimator = MiniBatchKMeans(n_clusters=n_clusters) ## Variation KMeans takes a set of samples iteratively compute distance from centroids for a random sample of instances
estimator.fit_transform(X_train_surf_features)

##create feature vectors of 300 dimensions for each instance of train and test sets
x_train = []

for instance in surf_features[:train_len]:
    #print(instance.size)
    for feature in instance:
        clusters = estimator.predict(instance)#Find the cluster associated with each of surf_descriptors
    features =np.bincount(clusters)#count them and append for one instance or image
    if (len(features)<n_clusters):
       features = np.append( features, np.zeros((1, n_clusters-len(features))))#add dimension of feature vecotr for each instance and fill with zero to make 300
    x_train.append(features)
       
x_test = []
for instance in surf_features[train_len:]:
    for feature in instance:
        clusters = estimator.predict(feature)
    features = np.bincount(clusters)
    if(len(features)<n_clusters):
       features = np.append(features, np.zeros((1, n_clusters-len(features))))
    x_test.append(features)


clf = LogisticRegression(C=0.001, penalty ='l2') # train the classifier (clf constant and normalization)
clf = clf.fit(x_train, y_train)

predictions = clf.predict(x_test)
print(classification_report(y_test, predictions))
print('Precission:', precision_score(y_test, predictions))
print('Recall', recall_score(y_test, predictions))
print('Accuracy', accuracy_score(y_test, predictions))
