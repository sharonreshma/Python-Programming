import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_md")

def analyze_sentence(sentence):
    doc = nlp(sentence)
    named_entities = [(ent.text, ent.label_) for ent in doc.ents]
    pos_tags = [(token.text, token.pos_, token.dep_, token.head.text) for token in doc]
    return named_entities, pos_tags

def visualize_sentence(sentence):
    doc = nlp(sentence)
    displacy.render(doc, style="ent")
    displacy.render(doc, style="dep")

def main():
    sentence = "In a groundbreaking study published in Nature, scientists have discovered a new species of deep-sea jellyfish, which glows in the dark, lives near hydrothermal vents, and feeds on microscopic organisms."
    named_entities, pos_tags = analyze_sentence(sentence)

    print("Named Entities:")
    for entity, label in named_entities:
        print(f"{entity} ({label})")

    print("\nPart-of-Speech Tags and Dependencies:")
    for word, pos, dep, head in pos_tags:
        print(f"{word} ({pos}) - {dep} -> {head}")

    visualize_sentence(sentence)

if __name__ == "__main__":
    main()
