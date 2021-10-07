from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
print(stemmer.stem('gathering'))

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('gathering','v'))
print(lemmatizer.lemmatize('gathering','n'))
