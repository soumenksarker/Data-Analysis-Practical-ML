from sklearn import preprocessing
import numpy as np
X=np.array([[0,5,6,7,8,9],[2,1,3,12,0,56],[1,2,3,4,5,6]])
print(preprocessing.scale(X))
