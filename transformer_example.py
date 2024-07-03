from transformers import BertForTokenClassification, BertTokenizer, pipeline

# Load pre-trained model and tokenizer
model_name = "SpanBERT/spanbert-large-cased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name)

# Example input text
text = "Alice and Bob are good friends. They enjoy playing chess together. Alice also likes reading books, and she often shares them with Bob."

# Tokenize input text
inputs = tokenizer(text, return_tensors="pt")

# Perform token classification
outputs = model(**inputs)

# Process token classification outputs
predictions = outputs.logits.argmax(dim=-1)
print("Token Classification Predictions:", predictions)

# Initialize NER pipeline
ner_pipeline = pipeline("ner", model=model_name, tokenizer=model_name)

# Perform NER
ner_results = ner_pipeline(text)
print("NER Results:", ner_results)
