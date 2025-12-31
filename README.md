# Text-To-Speech
A simple Python application that converts text input to speech using the pyttsx3 library. The program listens for user input and speaks it back aloud.
Features

Converts any text input to speech.
Customizable speech rate and volume.
Simple command-line interface.
Continuous conversation loop until exit.

Requirements

Python 3.x
pyttsx3 library

Installation

Clone or download this repository
Install the required dependency:

bashpip install pyttsx3
Usage
Run the program from the command line:
bashpython main.py
```

The program will prompt you with "You: " where you can type any text. The AI will speak back whatever you type.

### Commands

- Type any text and press Enter - The program will speak your text aloud
- Type `exit` or `quit` - The program will say "Goodbye" and terminate

## Configuration

You can modify the speech properties in the code:

- **Rate**: `engine.setProperty('rate', 150)` - Controls speech speed (words per minute)
- **Volume**: `engine.setProperty('volume', 1)` - Controls volume level (0.0 to 1.0)

## Example
```
You: Hello, how are you today?
[AI speaks: "Hello, how are you today?"]

You: This is a test
[AI speaks: "This is a test"]

You: exit
[AI speaks: "Goodbye"]
How It Works

The program initializes the pyttsx3 text-to-speech engine
Sets default voice properties (rate and volume)
Enters a continuous loop waiting for user input
Converts each input to speech using the speak() function
Exits when the user types 'exit' or 'quit'

License
This project is open source and available for educational purposes.Claude is AI and can make mistakes. Please double-check responses. Sonnet 4.5
