#Component Data NER

#global variables
import spacy
from spacy.tokens import Span
class CustomNERComponent:
    def __init__(self, nlp, custom_data):
        self.custom_data = custom_data

    def __call__(self, doc):
        entities = []
        for ent_text, label in self.custom_data["entities"].items():
            start = doc.text.find(ent_text)
            if start != -1:
                end = start + len(ent_text)
                span = doc.char_span(start, end, label=label)
                if span:
                    entities.append(span)
        doc.ents = entities
        return doc
custom_data = {
    "entities": {
        "Apple": "ORG",
        "Tim Cook": "PERSON",
        "Cupertino": "GPE"
    }
}
nlp = spacy.load("en_core_web_sm")
custom_ner = CustomNERComponent(nlp, custom_data)
nlp.add_pipe(custom_ner, last=True)
text = "Tim Cook, the CEO of Apple, unveiled new products in Cupertino."
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)


#class component data
import spacy
from spacy.tokens import Span
class CustomNERComponent:
    def __init__(self, nlp, custom_data):
        self.custom_data = custom_data

    def __call__(self, doc):
        entities = []
        for ent_text, label in self.custom_data["entities"].items():
            start = doc.text.find(ent_text)
            if start != -1:
                end = start + len(ent_text)
                span = doc.char_span(start, end, label=label)
                if span:
                    entities.append(span)
        doc.ents = entities
        return doc
custom_data = {
    "entities": {
        "Google": "ORG",
        "John Doe": "PERSON",
        "San Francisco": "GPE"
    }
}
nlp = spacy.load("en_core_web_sm")
custom_ner = CustomNERComponent(nlp, custom_data)
nlp.add_pipe(custom_ner, last=True)
text = "John Doe from Google visited San Francisco."
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)
