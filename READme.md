# TARS-Bot

TARS-Bot is an AI-powered chatbot inspired by the TARS robot from *Interstellar*. This chatbot is designed to be dynamic, responding with different personalities based on humor levels, technical knowledge, and detected user emotions.

## Features

- **Personalized User Interaction**: Remembers the user's name and adapts responses accordingly.
- **Emotion Detection**: Adjusts responses based on detected emotions (happy, sad, angry, neutral).
- **Humor & Technical Knowledge Levels**: Customizable humor and knowledge levels to tailor chatbot responses.
- **AI-Powered Responses**: Uses `meta-llama/Llama-3.3-70B-Instruct-Turbo` to generate context-aware responses.

## Installation

### Prerequisites

- Python 3.x
- `pip3` installed
- A virtual environment (recommended)

### Steps

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/TARS-Bot.git
   cd TARS-Bot
   ```
2. Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```sh
   pip3 install -r requirements.txt
   ```

## Usage

Run the chatbot with:

```sh
python basic.py
```

The chatbot will ask for your name and start responding to inputs dynamically based on the AI model.

## Customization

- Adjust `humor_level` and `technical_level` in `basic.py` to modify the chatbot's personality.
- Modify `detect_emotion` function to improve emotion recognition.
- Use a different AI model by updating the `model` parameter in API calls.

