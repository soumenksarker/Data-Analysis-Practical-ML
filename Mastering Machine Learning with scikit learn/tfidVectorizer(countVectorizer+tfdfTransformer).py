##TfidVectorizer(CountVectorizer, tfdf_transformer)product of this twos(Tf_dfTransformer retrieved inverse_documents_features used two mitigate the size problem in documents file where frequency of words occuring in two documensts  but dissimmilar due one documenst is larger than other
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = ['this is my first sample','and not the last one', 'this misssion commenced from now']
vectorizer = TfidfVectorizer()
print(vectorizer.fit_transform(corpus).todense())
#print(vectorizer.vocavulary_)
