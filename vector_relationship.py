import spacy
import numpy as np
nlp = spacy.load("en_core_web_md")

def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)

def find_similar_words(word, top_n=5):
    word_vector = nlp.vocab[word].vector
    similarity_scores = []

    for vocab_word in nlp.vocab:
        if vocab_word.has_vector and vocab_word.is_lower:
            similarity = cosine_similarity(word_vector, vocab_word.vector)
            similarity_scores.append((vocab_word.text, similarity))
    
    similarity_scores = sorted(similarity_scores, key=lambda item: -item[1])
    print(f"Words similar to '{word}':")
    for similar_word, score in similarity_scores[:top_n]:
        print(f"{similar_word} (Score: {score:.4f})")
    print()

def find_analogy(word1, word2, word3, top_n=1):
    """Find the word that completes the analogy: word1 - word2 + word3."""
    vector1 = nlp.vocab[word1].vector
    vector2 = nlp.vocab[word2].vector
    vector3 = nlp.vocab[word3].vector
    target_vector = vector1 - vector2 + vector3

    similarity_scores = []

    for vocab_word in nlp.vocab:
        if vocab_word.has_vector and vocab_word.is_lower:
            similarity = cosine_similarity(target_vector, vocab_word.vector)
            similarity_scores.append((vocab_word.text, similarity))
    
    similarity_scores = sorted(similarity_scores, key=lambda item: -item[1])
    print(f"Analogy: {word1} - {word2} + {word3} = ?")
    for similar_word, score in similarity_scores[:top_n]:
        print(f"{similar_word} (Score: {score:.4f})")
    print()

def compare_verb_tenses(verb_present, verb_past, verb_future):
    """Compare the similarity between verbs in different tenses."""
    vector_present = nlp.vocab[verb_present].vector
    vector_past = nlp.vocab[verb_past].vector
    vector_future = nlp.vocab[verb_future].vector

    similarity_past_present = cosine_similarity(vector_present, vector_past)
    similarity_present_future = cosine_similarity(vector_present, vector_future)

    print(f"Similarity between '{verb_present}' and '{verb_past}': {similarity_past_present:.4f}")
    print(f"Similarity between '{verb_present}' and '{verb_future}': {similarity_present_future:.4f}")
    print()

def process_sentence(sentence):
    """Extracts verbs and nouns from a sentence."""
    doc = nlp(sentence)
    verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
    nouns = [token.lemma_ for token in doc if token.pos_ == "NOUN"]
    return verbs, nouns

def main():
    sentence = "The quick brown fox jumps over the lazy dog, and then it runs around the field, barking loudly and chasing its tail."
    verbs, nouns = process_sentence(sentence)
    print(f"Verbs: {verbs}")
    print(f"Nouns: {nouns}")
    if nouns:
        find_similar_words(nouns[0])
    if len(nouns) >= 3:
        find_analogy(nouns[0], nouns[1], nouns[2])
    if verbs:
        compare_verb_tenses(verbs[0], verbs[0] + "ed", "will " + verbs[0])

if __name__ == "__main__":
    main()
