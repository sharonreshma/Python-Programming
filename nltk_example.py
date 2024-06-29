#nltk

#tokenizer
from nltk.tokenize import word_tokenize,sent_tokenize
text = "By tokenizing, you can conveniently split up text by word or by sentence. This will allow you to work with smaller pieces of text that are still relatively coherent and meaningful even outside of the context of the rest of the text. It’s your first step in turning unstructured data into structured data, which is easier to analyze."
tokens = word_tokenize(text)
t=sent_tokenize(text)
print(tokens)
print(t)

#stop words
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def remove_stopwords(text):
    word = word_tokenize(text)
    stop = set(stopwords.words('english'))
    filtered_text = [word for word in word if word.lower() not in stop]
    return filtered_text
if __name__ == "__main__":
    text = "This is a sample sentence, showing off the stop words filtration."
    filtered_text = remove_stopwords(text)
    print("Original Text:", text)
    print("Filtered Text:", " ".join(filtered_text))


from janome.tokenizer import Tokenizer
japanese_stopwords = [
    "の", "に", "は", "を", "た", "が", "で", "て", "と", "し", "れ", "さ", "ある", 
    "いる", "も", "する", "から", "な", "こと", "として", "その", "それ", "この", 
    "もの", "という", "など", "なっ", "ので", "よう", "そして", "おり", "より", 
    "また", "または", "です", "ます", "これ", "あれ", "ここ", "そこ", "あそこ", 
    "どう", "そう", "あと", "ほか", "さらに"
]

def remove_japanese_stopwords(text):
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text, wakati=True)
    filtered_tokens = [token for token in tokens if token not in japanese_stopwords]
    return filtered_tokens

if __name__ == "__main__":
    text = "これはサンプルの文章です。ストップワードを除去します。"
    filtered_text = remove_japanese_stopwords(text)
    print("Original Text:", text)
    print("Filtered Text:", " ".join(filtered_text))

#stemming
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
 
ps = PorterStemmer()
words = ["program", "programs", "programmer", "programming", "programmers"] 
for w in words:
    print(w, " : ", ps.stem(w))

sentence = "Programmers program with programming languages"
words = word_tokenize(sentence)
 
for w in words:
    print(w, " : ", ps.stem(w))
    
#parts of speech
import nltk
from nltk.tokenize import word_tokenize
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
sentence = "Natural language processing is fascinating."
words = word_tokenize(sentence)
pos_tags = nltk.pos_tag(words)
print("Words:", words)
print("POS Tags:", pos_tags)


#lemmantize
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))
print("better :", lemmatizer.lemmatize("better",pos="a"))

#chunking and chinking
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, RegexpParser
sentence = "The quick brown fox jumps over the lazy dog."
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)
grammar = r"""
  NP: {<DT>?<JJ>*<NN>}    # Chunk sequences of DT, JJ, NN
      {<NNP>+}           # Chunk consecutive proper nouns
"""
chink_grammar = r"""
  NP: {<.*>+}             # Chunk everything
      }<VBZ|IN>+{         # Chink sequences of VBZ or IN
"""
chunk_parser = RegexpParser(grammar)
chink_parser = RegexpParser(chink_grammar)
chunked_tokens = chunk_parser.parse(tagged_tokens)
chinked_tokens = chink_parser.parse(tagged_tokens)
# Print the chunked tokens (can also visualize or iterate over the tree)
print(chunked_tokens)
print(chinked_tokens)
