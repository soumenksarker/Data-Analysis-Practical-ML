from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('ggplot')
##
##xs = np.array([1,2,3,4,5], dtype = np.float64)
##ys = np.array([5,4,6,5,6], dtype = np.float64)
def create_dataset(hm, variance, step = 2, correlation = False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation =='pos':
            val += step
        elif correltion and correlation == 'neg':
            val -= step
    xs = [i for i in range(len(ys))]
    return np.array(xs, dtype = np.float64), np.array(ys, dtype = np.float64)

xs, ys = create_dataset(40, 40, 2, correlation = 'pos') ##just change the variance U should get the tightly fit of dataset and test the co-efficient of determination(r^2)

def best_fit_slope_and_intercept(xs, ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)*mean(xs)) - mean(xs*xs)))
    b = mean(ys) - m*mean(xs)
    return m, b

def squared_error(ys_orig, ys_line):
    return sum((ys_line - ys_orig)*(ys_line-ys_orig))

def coefficient_of_determination(ys_orig, ys_line):
    ys_mean_line   = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, ys_mean_line)
    return 1 - (squared_error_regr/squared_error_y_mean )

m,b = best_fit_slope_and_intercept(xs, ys)

regression_line = [(m*x)+b for x in xs]
r_squared = coefficient_of_determination(ys, regression_line)
##predict_x = xs
##predict_y = (m*predict_x)
plt.scatter(xs, ys)
plt.plot(xs, regression_line)
##plt.scatter(predict_x, predict_y, color = 'g')
print(r_squared)
plt.show()

