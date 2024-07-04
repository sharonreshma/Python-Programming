import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

# Grammar rule
grammar = CFG.fromstring("""
  S -> NP VP
  NP -> DT NN
  VP -> VBZ NP
  DT -> 'the' | 'a'
  NN -> 'cat' | 'dog'
  VBZ -> 'chases' | 'sees'
""")

parser = RecursiveDescentParser(grammar)
def check_grammar(sentence):
    tokens = nltk.word_tokenize(sentence)
    
    try:
        parse_trees = list(parser.parse(tokens))
        if parse_trees:
            print("The sentence is grammatically correct.")
            for tree in parse_trees:
                tree.pretty_print()
        else:
            print("The sentence does not conform to the defined grammar rules.")
    except ValueError as e:
        print(f"Parsing error: {e}")

sentence = "the cat chases the dog"
check_grammar(sentence)