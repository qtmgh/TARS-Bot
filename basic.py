import random
from datetime import datetime

# Initialize a variable to store the user's name
user_name = None

# Define chatbot personality
humor_level = 0.6 # Adjustable between 0 and 1

# Define responses
responses = {"hello": ["Hello, human.", "Greetings, Earthling.", "TARS online. How may I assist?"], 
             "time dilation": ["Time is relative. Where are you going?", "Depends on your velocity and gravity."], 
             "mission": ["Your mission is to survive. Adapt. Explore."],
             "joke": ["Knock knock, who's there? Not Cooper, he's in a black hole."]}

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
        get_user_name() # Ask for user's name at the start!

    input_text = input_text.lower()

    # Check if input matches a key
    for key in responses:
        if key in input_text:
            if key == "joke":
                return random.choice(responses[key]) if random.random() < humor_level else "Humor setting too low."
            return random.choice(responses[key])
            
    return "I'm afraid I can't do that, Dave. (Oh wait, wrong AI...)"

def main(): 
    get_user_name() # Asks user for name at the start
    print(f"TARS: {get_time_of_day()}, {user_name}.") # Time based greeting

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