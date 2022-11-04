from textblob import TextBlob
import pyttsx3
import speech_recognition as sr
import randfacts
import pyjokes
engine = pyttsx3.init()
r = sr.Recognizer()
def sentiScore(data):
    x=TextBlob(data)
    return x.sentiment.polarity
def speak(line):
    print("AI - ",line)
    engine.say(line)
    engine.runAndWait()
def listen():
    with sr.Microphone() as source:
        print("listening")
        r.adjust_for_ambient_noise(source, 1.2)
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
        return text
def ifHappy():
    speak("I think you are happy")
def ifNuetral():
    speak("You do not seem sad but anyways I hope you will be happier")
def ifSad():
    speak("You do seem sad. Would you like to know a fact or listen a joke or none of them?")
    demand=listen()
    if "fact" in demand or "facts" in demand:
        x = randfacts.get_fact()
        speak(x)
    elif "joke" in demand or "jokes" in demand:
        My_joke = pyjokes.get_joke(language="en", category="all")
        speak(My_joke)
    elif "no" in demand or "none" in demand or "nothing" in demand:
        speak("ok then I hope you will be happier")
    else:
        speak("ok then I hope you will be happier")    
while True:
    speak("How do you feel today?")
    speech=listen()
    value =sentiScore(speech)
    if value<0:
        ifSad()
    elif value==0:
        ifNuetral()
    elif value>0:
        ifHappy()