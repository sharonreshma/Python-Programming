import spacy
from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
pattern = [
    {"LOWER": "the"},
    {"LOWER": {"IN": ["quick", "lazy"]}},  # Match "quick" or "lazy"
    {"POS": "ADJ"},  # Adjective like "brown"
    {"LOWER": "fox"},
    {"LOWER": "jumps"},
    {"LOWER": "over"},
    {"LOWER": "the"},
    {"LOWER": "lazy"},
    {"LOWER": "dog"}
]

matcher.add("COMPLEX_PATTERN", [pattern])
doc = nlp("the quick brown fox jumps over the lazy dog. The lazy brown fox jumps over the quick dog.")
matches = matcher(doc)
if matches:
    for match_id, start, end in matches:
        span = doc[start:end]
        print(f"Match found: {span.text}")
else:
    print("No matches found")
