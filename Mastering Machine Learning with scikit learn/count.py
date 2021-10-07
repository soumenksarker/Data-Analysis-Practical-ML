from sklearn.feature_extraction import CountVectorizer
corpus = ['The dog ate a sandwich, the wizerd transfigured a sandwich, and I ate a sandwich']
vectorizer = CountVectorizer(stop_words='english')
print vectorizer.fit_transform(corpus).todense()
