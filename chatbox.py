
def chatbot():
    print("Chatbot 🤖: Hi! I am your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower().strip()

        # Rule-based replies
        if user_input in ["hi", "hello"]:
            print("Chatbot 🤖: Hello! How can I help you?")
        elif user_input in ["how are you", "how r u", "how are u"]:
            print("Chatbot 🤖: I'm doing great, thank you! How about you?")
        elif user_input in ["i am fine", "i'm fine", "fine"]:
            print("Chatbot 🤖: That's good to hear! 😊")
        elif user_input in ["thanks", "thank you"]:
            print("Chatbot 🤖: You're welcome! 👍")
        elif user_input in ["bye", "goodbye"]:
            print("Chatbot 🤖: Goodbye! Have a nice day 👋")
            break
        else:
            print("Chatbot 🤖: Sorry, I didn’t understand that. Can you rephrase?")
chatbot()