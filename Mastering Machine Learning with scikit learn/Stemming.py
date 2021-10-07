from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
example_text = ['python', 'pythoner ', 'pythonly',' pythonisht', 'pythoned','gathering', 'gathering', 'pythoning']
ps = PorterStemmer()
for w in example_text:
    print(ps.stem(w))
