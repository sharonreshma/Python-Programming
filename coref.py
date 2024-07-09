#implementing neuarcoref

import spacy
import neuralcoref
nlp = spacy.load('en_core_web_sm')
neuralcoref.add_to_pipe(nlp)
doc1 = nlp('My sister has a dog. She loves him.')
print(doc1._.coref_clusters)
doc2 = nlp('Angela lives in Boston. She is quite happy in that city.')
for ent in doc2.ents:
    print(ent._.coref_cluster)
    

#complex sentence coref    
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
print("\nCoreference resolution in the text:")
if doc._.has_coref:
    resolved_text = doc._.coref_resolved
    print("Resolved text:", resolved_text)
    for cluster in doc._.coref_clusters:
        print(f"Cluster: {cluster}")
else:
    print("No coreferences found.")
    
    
#allenlp
import spacy
from allennlp.predictors.predictor import Predictor
import allennlp_models.coref
nlp = spacy.load('en_core_web_sm')
predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2021.03.10.tar.gz")
text = "My sister has a dog. She loves him."
doc = nlp(text)
result = predictor.predict(document=text)
coref_clusters = result['clusters']
print(coref_clusters)
