import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome to SpeakerBot v1.1")
    while True:
        x = input("Enter what you want me to speak: ")
        speak(x)
