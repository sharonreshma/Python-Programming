from transformers import pipeline

# Load pre-trained model and tokenizer
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# Start conversation
print("Chatbot: Hi! How can I help you?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot(user_input)
    print("Chatbot:", response[0]['generated_text'])

