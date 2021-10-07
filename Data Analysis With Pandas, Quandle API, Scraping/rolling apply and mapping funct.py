import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from statistics import mean
style.use('fivethirtyeight')

housing_data = pd.read_pickle('HPI.pickle2')
housing_data = housing_data.pct_change()


housing_data.replace([np.inf, -np.inf], np.nan, inplace=True)
housing_data['US_HPI_future'] = housing_data['US_HPI'].shift(-1)
housing_data.dropna(inplace=True)

def create_labels(cur_hpi, fut_hpi):
    if fut_hpi > cur_hpi:
        return 1
    else:
        return 0
def moving_average(values):
    ma = mean(values)
    return ma
housing_data['label'] = list(map(create_labels,housing_data['US_HPI'], housing_data['US_HPI_future']))
print(housing_data[['US_HPI_future' ,'US_HPI']].head())

housing_data['ma_apply_example'] = pd.rolling_apply(housing_data['M30'], 10, moving_average)
print(housing_data.tail())
