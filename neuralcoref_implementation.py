import spacy
import neuralcoref
from spacy import displacy
from textblob import TextBlob

nlp = spacy.load('en_core_web_sm')

neuralcoref.add_to_pipe(nlp)

text = """
Alice, who lives in Paris, loves reading. She has a friend named Bob who also loves books. 
One day, when Alice was at the library, she saw Bob. He was looking for a book that Alice had recommended to him. 
Bob was excited to find the book because he had heard great things about it. 
Meanwhile, Alice received a call from her sister, who told her about a new book club. 
She wanted Alice to join it, but Alice wasn't sure if she had the time. 
After talking to her sister, Alice decided to go back and talk to Bob about the book club. 
Bob thought it was a great idea and suggested they join together.
"""

doc = nlp(text)

print("\nPOS in the text:")
for token in doc:
    print(f"{token.text} : {token.pos_} : {spacy.explain(token.tag_)}")

print("\nNER in the text:")
for ent in doc.ents:
    print(f"{ent.text} : {ent.label_}")

print("\nSentiment in the text:")
blob = TextBlob(doc.text)
print(f"Sentiment: {blob.sentiment}")

print("\nCoreference resolution in the text:")
if doc._.has_coref:
    resolved_text = doc._.coref_resolved
    print("Resolved text:", resolved_text)
    for cluster in doc._.coref_clusters:
        print(f"Cluster: {cluster}")
else:
    print("No coreferences found.")

displacy.serve(doc, style="ent")
