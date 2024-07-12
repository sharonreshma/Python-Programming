import spacy
nlp = spacy.load("en_core_web_sm")
# Complex sentence example
sentence = """
The ancient castle, with its towering spires and labyrinthine corridors, concealed a treasure that had eluded explorers for centuries. 
Legends spoke of a mystical gem, imbued with the power to grant its possessor immortality, hidden within the castle's depths.
Countless adventurers had sought the gem, only to vanish without a trace, adding to the castle's aura of mystery and danger.
However, a renowned historian, Professor Emily Roberts, claimed to have deciphered clues pointing to the gem's location, buried beneath the castle's oldest tower.
Joined by a team of archaeologists and expert climbers, Professor Roberts embarked on a perilous expedition to uncover the truth behind the legends.
"""
doc = nlp(sentence)
def extract_relationships(doc):
    relationships = []
    for token in doc:
        if token.dep_ in ("attr", "dobj"):
            subject = [w.text for w in token.head.lefts if w.dep_ == "nsubj"]
            if subject:
                relationships.append((subject[0], token.text))
    return relationships
relationships = extract_relationships(doc)
print("Relationships:", relationships)
