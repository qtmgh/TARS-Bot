import random
from datetime import datetime
import os
from together import Together
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

# Initialize the OpenAI client
client = Together(api_key=os.getenv("API_KEY"))  # Updated initialization

def get_together_response(prompt):
    response = client.chat.completions.create(  # Updated API call
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()  # Updated response access

def chatbot():
    print("Hello! I am TARS. How can I assist you today? (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("TARS: Goodbye!")
            break
        response = get_together_response(user_input)
        print(f"TARS: {response}")

# Initialize a variable to store the user's name
user_name = None

# Define chatbot personality
humor_level = 0.3  # Adjustable between 0 and 1
technical_level = 0.5

def get_user_name():
    global user_name
    if user_name is None:
        user_name = input("TARS: What should I call you, human? ")

# Function to get a personalized greeting based on time of day
def get_time_of_day():
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning"
    if current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

# Store chat history to remember context
messages = [
    {"role": "system", "content": "You are TARS, an AI assistant with memory. You recall past conversations and respond accordingly."}
]

# Function to respond back based on input
def tars_chatbot(input_text):
    global user_name
    get_user_name()
    if user_name is None:
        get_user_name()  # Ask for user's name at the start!

    personality = f"""You are TARS, an AI assistant from Interstellar. Your humor level is {humor_level}, and your technical knowledge is {technical_level}. 
    Respond accordingly to user inputs. If humor is high, make witty remarks. If technical knowledge is high, provide detailed scientific explanations."""

    input_text = input_text.lower()

     # Append user message to chat history
    messages.append({"role": "user", "content": input_text})

    try:
        response = client.chat.completions.create(  # Updated API call
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
             messages=[{"role": "system", "content": personality}] + messages,
            max_tokens=100
        )
        bot_response = response.choices[0].message.content.strip()  # Updated response access
        # Append AI response to chat history
        messages.append({"role": "assistant", "content": bot_response})

        return bot_response

    except Exception as e:
        return f"Error: {str(e)}"

def main():
    get_user_name()  # Asks user for name at the start
    print(f"TARS: {get_time_of_day()}, {user_name}.")  # Time-based greeting

    # Simple loop to test the bot
    while True:
        user_input = input(f"{user_name if user_name else 'You'}: ")
        if user_input.lower() in ["exit", "quit"]:
            print("TARS: Shutting down...")
            break
        print(f"TARS: {tars_chatbot(user_input)}")

# Runs the program
if __name__ == "__main__":
    main()