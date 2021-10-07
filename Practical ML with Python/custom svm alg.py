import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')


class Support_Vector_Machine():
    def __init__(self, visualization)
    self.visualization = visualization
    self.colors = {1:'r', -1:'b'}
    if self.visualization:
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1,1,1)

    #train

    def fit(self, data):
        self.data = data
        opt_dict = {}
        transforms = [[1,1],[1,-1],[-1,1],[-1,-1]]
        
        #finding the value to work with our range

        all_data = []
        for yi in  self.data:
            for featureset self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)
        self.max_feature_value = max_value(all_data)
        self.min_feature_value = min_value(all_data)
        #no need to keep in memory
        all_data = None
        step_size= [self.max_feature_value*0.1,
                    self.max_feature_value*0.01,
                    #starts getting very high cost after this.
                    self.max_feature_value*0.001]
        b_range_multiple = 5
        b_multiple = 5
        latest_optimal = self.max_features_value*10
        for step in step_size:
            w= np.array([latest_optimal, latest_optimal])
            # we can do this cause of convex optimization value
            optimized = False
            while not optimized:
                pass
    def predict(self, features):
        #sign(x.w+b)
     classification = np.sign(np.dot(np.array(features), self.w)+ self.b)
     return classification

data_dict = { -1:np.array([[1,7],[2,8],[3,8],]),
              1:np.array([[5,1],[6,-1],[7,3],])}


