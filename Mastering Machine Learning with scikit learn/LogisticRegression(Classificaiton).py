import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score##the deprecation warning raised due to the cross_validation is auto updated in latest module
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression


df = pd.read_csv("SMSSpamCollection.csv", sep = '\t', header = None)
print ('Number of spam messages:', df[df[0] == 'spam'][0].count())
print ('Number of ham messages:', df[df[0] == 'ham'][0].count())
#df.reset_index(drop=True)
#print(df.describe())
##print(df[0])
##print(df[1])
X= df['label']=df[0]
y=df['message']=df[1]

X_train_raw,x_test_raw, y_train,y_test = train_test_split(X,y)

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train_raw)
x_test = vectorizer.transform(x_test_raw)


classifier = LogisticRegression(n_jobs =-1)
classifier.fit(X_train, y_train)
predictions = classifier.predict(x_test)
for i, prediction in enumerate(predictions[:5]):
       print('Prediction:%s. Message: %s' %(prediction, x_test_raw[i]))

