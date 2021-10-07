import quandl
import pandas as pd
import pickle

import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = open("quandlapikey.txt",'r').read()

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]
        
def grab_initial_state_data():
    states = state_list()
    
    main_df = pd.DataFrame()
    for abbv in states:
        #print(abbv)
        
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, auth_token = api_key)
        df.columns = [str(abbv)]
        #df = df.pct_change()
        df[abbv] = (df[abbv] - df[abbv][0])/df[abbv][0]*100.0
        
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
            
    print(main_df.head())
    pickle_out = open('fiddy_states4.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()
    
##grab_initial_state_data()
##HPI_data = pd.read_pickle('fiddy_states4.pickle')
#print(HPI_data)
#HPI_data['TX2'] = HPI_data['TX']*2

##def HPI_Benchmark():
##    df = quandl.get('FMAC/HPI_USA', auth_token = api_key)
##    df['Value'] = (df['Value'] - df['Value'][0])/df['Value'][0]*100.0
##    return df
##fig = plt.figure()
##ax1 = plt.subplot2grid((1,1),(0,0))

HPI_data = pd.read_pickle('fiddy_states4.pickle')
HPI_data['TX1yr'] = HPI_data['TX'].resample('A')
print(HPI_data[['TX','TX1yr']])
##HPI_data['Tx1yr'].plot('monthly pricr per state', color = 'k', linewidth = 10)
##plt.show()

##
##benchmark = HPI_Benchmark()
##
##HPI_data.plot(ax=ax1)
##benchmark.plot(color = 'k',ax = ax1, linewidth = 10)
##plt.legend().remove()
##plt.show()
##HPI_data_correlation = HPI_data.corr()
##print(HPI_data_correlation)
##print(HPI_data_correlation.describe())
#print(HPI_data[['TX','TX2']].head())
