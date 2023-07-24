import requests
import json
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

city=input("Enter the name of the city\n ")
url= f"https://api.weatherapi.com/v1/current.json?key=3f5effc010924b49881110231230107&q={city}"
r= requests.get(url)  
# print(r.text)
wDic=json.loads(r.text)
speak("Temperature is")
speak(wDic["current"]["temp_c"])
speak("and the humidity is")
speak(wDic["current"]["humidity"])
speak("and it feels like")
speak(wDic["current"]["feelslike_c"])
print("Temperature is")
print(wDic["current"]["temp_c"])
print("and the humidity is")
print(wDic["current"]["humidity"])
print("and it feels like")
print(wDic["current"]["feelslike_c"])
