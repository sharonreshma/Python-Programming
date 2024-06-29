import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data files
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Sharon.",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem",]
    ],
    [
        r"I am fine",
        ["Great to hear that", "How can I help you?",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ],
]

# Default reflections (you can customize these)
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Create Chat object
chatbot = Chat(pairs, reflections)

# Start conversation
def chatbot_response(user_input):
    return chatbot.respond(user_input)

# Test chatbot
print("Chatbot: Hi! How can I help you?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
