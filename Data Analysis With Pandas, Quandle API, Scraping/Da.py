import pandas as pd
database = {'Supto' : ['Name:Soumen Sarker','Age: 20'],#, 'phone NO: 01795776460','District:Bogra','E-mail_Address: soumensarker.ice.iu.bd@gmail.com'],
            
            'Gupto' : ['Name:Gupto Sarker','Age:15']

            }
df =pd.DataFrame(database)
print(df)
df.set_index('Supto', inplace = True)
df.set_index('Gupto', inplace = True)
print(df)
