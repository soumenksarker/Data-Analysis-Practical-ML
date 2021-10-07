from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

xs = [1,2,3,4,5]
ys = [5,4,6,5,6]
xs = np.array([1,2,3,4,5], dtype = np.float64)
ys = np.array([5,4,6,5,6], dtype = np.float64)
##plt.scatter(xs, ys)
##plt.show()
def best_fit_slope_and_intercept(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)*mean(xs)) - mean(xs*xs)))
    
    b = mean(ys) - m*mean(xs)
    
    return m, b
m, b = best_fit_slope_and_intercept(xs, ys)
print(m,b)
regression_line = [(m*x)+b for x in xs]

import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

#plt.show()
predict_x = 8
predict_y = (m*predict_x) + b
print(predict_y)
plt.scatter(xs,ys,color = '#003F72', label = 'data')
plt.scatter(predict_x, predict_y, color = 'g')
plt.plot(xs,regression_line, label = 'Regression_line')
plt.legend(loc=4)
plt.show()
