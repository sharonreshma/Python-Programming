import spacy
import language_tool_python
nlp = spacy.load('en_core_web_sm')
tool = language_tool_python.LanguageTool('en-US')

# token & pos
def tokenize_and_tag(text):
    doc = nlp(text)
    tokens_pos = [(token.text, token.pos_) for token in doc]
    return tokens_pos

# tool
def check_grammar(text):
    matches = tool.check(text)
    return matches

# error corr
def suggest_corrections(matches, text):
    corrections = []
    for match in matches:
        corrections.append({
            'error': match.context,
            'message': match.message,
            'suggestions': match.replacements,
            'offset': match.offset,
            'length': match.errorLength
        })

    corrected_text = list(text)
    offset_diff = 0

    for correction in corrections:
        start = correction['offset'] + offset_diff
        end = start + correction['length']
        if correction['suggestions']:
            suggestion = correction['suggestions'][0]
            corrected_text[start:end] = suggestion
            offset_diff += len(suggestion) - correction['length']

    return corrections, ''.join(corrected_text)

def grammar_checker_corrector(text):
    tokens_pos = tokenize_and_tag(text)
    
    matches = check_grammar(text)
    corrections, corrected_text = suggest_corrections(matches, text)
    
    return tokens_pos, corrections, corrected_text

text = input("enter text: ")
tokens_pos, corrections, corrected_text = grammar_checker_corrector(text)

print("Tokens and POS Tags:")
for token, pos in tokens_pos:
    print(f"{token}: {pos}")

print("\nCorrections:")
for correction in corrections:
    print(f"Error: {correction['error']}")
    print(f"Message: {correction['message']}")
    print(f"Suggestions: {', '.join(correction['suggestions'])}\n")

print("Corrected Text:")
print(corrected_text)