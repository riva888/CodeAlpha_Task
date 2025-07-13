def get_bot_reply(user_input):
    user_input = user_input.lower()  # Make input case-insensitive
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I am fine, thanks."
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

def run_chatbot():
    print("Welcome to SimpleBot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        reply = get_bot_reply(user_input)
        print("Bot:", reply)
        if user_input.lower() == "bye":
            break

# Run the chatbot
run_chatbot()
