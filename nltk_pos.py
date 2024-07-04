import nltk
from nltk.tokenize import word_tokenize
sentence = "The quick brown fox jumps over the lazy dog"
words = word_tokenize(sentence)
tagged_words = nltk.pos_tag(words)
print(tagged_words)
