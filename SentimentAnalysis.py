from nltk.tokenize import sent_tokenize
from textblob import TextBlob
text="I am so sad. That I might be depressed but I am trying to happy and brighten my day. Lets live life to the fullest."
tokens=sent_tokenize(text)
pos_reviews=[]
neg_reviews=[]
for token in tokens:
    blob=TextBlob(token)
    senti=blob.sentiment
    pol_Points=senti.polarity
    subjec_points=senti.subjectivity
    if pol_Points>0:
        pos_reviews.append(token)
    else:
        neg_reviews.append(token)
print(len(pos_reviews),"positive reviews =>",pos_reviews)
print(len(neg_reviews),"negative commands =>",neg_reviews)