import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
#import numpy as np
web_stats = {
            'Day':[1,2,3,4,5,6],
            'Visitors':[43,53,34,45,64,34],
            'Bounce_Rate' :[78,57,34,45,64,34]
    }
df =pd.DataFrame(web_stats)
print(df)
df['Bounce_Rate'].plot()
plt.legend()
plt.show()
#print(df.head())
#print(df.tail())
#print(df.tail(2))

df.set_index('Day', inplace=True)
print(df.head())

##print(['Bounce Rate'])
##print(df.Visitors)
##
#print(np.array(df[['Bounce_Rate', 'Visitors']]))
print(df.Visitors.tolist())

