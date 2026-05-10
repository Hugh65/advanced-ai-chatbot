import datetime
import random

print("🤖 Advanced AI Chatbot Activated...\n")

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def mood_reply():
    replies = [
        "I'm doing great! Ready to help you 🚀",
        "Feeling smart today 🤖",
        "Always here to assist you 💡"
    ]
    return random.choice(replies)

def chatbot_response(user):

    user = user.lower()

    # Greetings
    if user in ["hi", "hello", "hey"]:
        return "Hello! How can I assist you today? 😊"

    # Time
    elif "time" in user:
        return f"Current time is ⏰ {get_time()}"

    # AI question
    elif "what is ai" in user:
        return "AI means Artificial Intelligence — machines that can think and learn like humans 🤖"

    # Mood
    elif "how are you" in user:
        return mood_reply()

    # Study help
    elif "study" in user:
        return "Focus 45 mins + 10 min break = best learning formula 📚"

    # Coding
    elif "python" in user:
        return "Python is a powerful programming language used in AI, web & automation 💻"

    # Bye
    elif user in ["bye", "exit", "quit"]:
        return "Goodbye! Keep building amazing things 🚀"

    # Default
    else:
        return "I'm still learning 🤖 but I will improve with more data!"

# Main loop
while True:
    user_input = input("\nYou: ")

    response = chatbot_response(user_input)
    print("Bot:", response)

    if user_input.lower() in ["bye", "exit", "quit"]:
        break