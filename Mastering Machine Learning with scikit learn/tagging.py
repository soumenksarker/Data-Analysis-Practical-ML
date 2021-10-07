import nltk
from nltk.tokenize import PunktSentenceTokenizer
train_text = "this is my first experience in python, and obviously i saw the devil!"
sample_text = "This is no my first attempt in python and i wanna get it crucialy"
custom_sentence_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sentence_tokenizer.tokenize(sample_text)
def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
       print(str(e))
process_content()
