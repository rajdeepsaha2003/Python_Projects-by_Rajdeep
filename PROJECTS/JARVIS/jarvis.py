import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
         speak("Good Morning!")
    elif hour >= 12 and hour < 18:
       speak("Good afternoon!")
    else:
        speak("Good Evening")

    speak("I am Jarvis, please tell SIR me how can I help You")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recocnizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e :
        print(e)

        print("Say That again...")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        #  logic for executingn task based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")

        elif 'open google' in query:
            webbrowser.open("Google.com")

        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open chat gpt' in query:
            webbrowser.open("chat.openai.com")
        
        elif 'play music' in query: 
            music_dir = ""C:\\Users\\rajde\\OneDrive\\Desktop\\PROJECTS\\JARVIS\\musics""
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strTime}")
            print(f"The time is{strTime}")
        
        elif 'code' in query:
            codepath = ""C:\\Users\\rajde\\OneDrive\\Desktop\\Visual Studio Code.lnk""
            os.startfile(codepath)
        elif 'very good' in query:
            speak("Thank You sir")

        