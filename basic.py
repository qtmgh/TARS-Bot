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
humor_level = 0.6  # Adjustable between 0 and 1

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

# Function to respond back based on input
def tars_chatbot(input_text):
    global user_name
    get_user_name()
    if user_name is None:
        get_user_name()  # Ask for user's name at the start!

    input_text = input_text.lower()

    try:
        response = client.chat.completions.create(  # Updated API call
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
            messages=[{"role": "system", "content": "You are TARS, a highly intelligent and witty AI assistant from Interstellar. You are logical, helpful, and occasionally humorous."},
                      {"role": "user", "content": input_text}],
            max_tokens=100
        )
        return response.choices[0].message.content.strip()  # Updated response access

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