# chatbot.py
from rules import rules

def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in rules:
        if key in user_input:
            return rules[key]
    return "Sorry, I don't understand that yet."

# Main loop
print("Chatbot: Hi! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot:", rules["bye"])
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
