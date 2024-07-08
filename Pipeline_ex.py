#PIPELINING

#processing text in pipelining
import spacy
nlp = spacy.load("en_core_web_sm")
text = "Apple is looking at buying U.K. startup for $1 billion"
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)
    

#pipeline concept nlp.pipe
import spacy

texts = [
    "Net income was $9.4 million compared to the prior year of $2.7 million.",
    "Revenue exceeded twelve billion dollars, with a loss of $1b.",
]

nlp = spacy.load("en_core_web_sm")
for doc in nlp.pipe(texts, disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"]):
    print([(ent.text, ent.label_) for ent in doc.ents])
    
#nlp as_tuple
import spacy
from spacy.tokens import Doc

if not Doc.has_extension("text_id"):
    Doc.set_extension("text_id", default=None)

text_tuples = [
    ("Last Wednesday, John Doe, a software engineer at Google, met with Jane Smith, the CEO of a small AI startup, to discuss a potential acquisition.", {"text_id": "text1"}),
    ("The meeting, which took place at a popular café in San Francisco, lasted for over two hours.", {"text_id": "text2"})
]

nlp = spacy.load("en_core_web_sm")
doc_tuples = nlp.pipe(text_tuples, as_tuples=True)

docs = []
for doc, context in doc_tuples:
    doc._.text_id = context["text_id"]
    docs.append(doc)

for doc in docs:
    print(f"{doc._.text_id}: {doc.text}")

 
 #Custom Components
import spacy
from spacy.tokens import Token, Span
def custom_token_attribute(doc):
    for token in doc:
        token._.is_custom = len(token.text) > 5
    return doc
def custom_ner_component(doc):
    custom_entities = {
        "Google": "ORG",
        "John Doe": "PERSON",
        "San Francisco": "GPE"
    }
    entities = []
    for ent_text, label in custom_entities.items():
        start = doc.text.find(ent_text)
        if start != -1:
            end = start + len(ent_text)
            span = doc.char_span(start, end, label=label)
            if span:
                entities.append(span)
    doc.ents = entities
    return doc
Token.set_extension('is_custom', default=False)
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe(custom_token_attribute, last=True)
nlp.add_pipe(custom_ner_component, last=True)
texts = [
    "Last Wednesday, John Doe, a software engineer at Google, met with Jane Smith, the CEO of a small AI startup, to discuss a potential acquisition.",
    "The meeting, which took place at a popular café in San Francisco, lasted for over two hours.",
    "During their conversation, they talked about the impact of AI on healthcare, the future of autonomous vehicles, and the role of ethical considerations in technology development.",
    "Microsoft announced a new AI-powered tool that aims to help developers write code more efficiently and accurately, potentially transforming software development practices.",
    "Elon Musk's SpaceX successfully launched its latest batch of Starlink satellites into orbit, further expanding its satellite internet service.",
    "The COVID-19 pandemic has accelerated the adoption of remote work, leading to significant changes in how businesses operate and how employees collaborate."
]
for text in texts:
    doc = nlp(text)
    print(f"\nText: {doc.text}")
    for token in doc:
        print(token.text, token._.is_custom)
    for ent in doc.ents:
        print(ent.text, ent.label_)
        
           
#multiprocess
import spacy
nlp = spacy.load("en_core_web_sm")
texts = [
    "Last Wednesday, John Doe, a software engineer at Google, met with Jane Smith, the CEO of a small AI startup, to discuss a potential acquisition. The meeting, which took place at a popular café in San Francisco, lasted for over two hours.",
    "During their conversation, they talked about the impact of AI on healthcare, the future of autonomous vehicles, and the role of ethical considerations in technology development.",
    "Microsoft announced a new AI-powered tool that aims to help developers write code more efficiently and accurately, potentially transforming software development practices.",
    "Elon Musk's SpaceX successfully launched its latest batch of Starlink satellites into orbit, further expanding its satellite internet service.",
    "The COVID-19 pandemic has accelerated the adoption of remote work, leading to significant changes in how businesses operate and how employees collaborate."
]

docs = list(nlp.pipe(texts, n_process=2))
for doc in docs:
    print(f"\nText: {doc.text}")
    for ent in doc.ents:
        print(ent.text, ent.label_)
        
@spacy.registry.misc("acronyms.slang_dict.v1")
def create_acronyms_slang_dict():
    dictionary = {"lol": "laughing out loud", "brb": "be right back"}
    dictionary.update({value: key for key, value in dictionary.items()})
    return dictionary

