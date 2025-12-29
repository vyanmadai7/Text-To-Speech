#import text to speech library
import pyttsx3

#initialize the TTS engine
engine = pyttsx3.init()

#set voice properties
engine.setProperty('rate', 150)  # words per minute
engine.setProperty('volume', 1)  # volume

#function to make the AI speak
def speak(text):
    engine.say(text)
    engine.runAndWait()  # play the speech

#main program
if __name__ == "__main__":
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['exit', 'quit']:
            speak("Goodbye")  # says goodbye and stops
            break
        speak(user_input)  # repeats what you said
