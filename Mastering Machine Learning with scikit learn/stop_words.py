from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
example = "this is my starting of python, the weather is good!And python is awesome"

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example)
#filtered_sentence = [w for w in word_tokens if  w not in stop_words]

filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
for i in word_tokens:
 print(i)
 
for s in filtered_sentence:
 print(s)
