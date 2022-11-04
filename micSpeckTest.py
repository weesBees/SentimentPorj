import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
r = sr.Recognizer()
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
        return text

while True:
    speak("How do you feel today?")
    speech=listen()
    if "no" in speech:
        speak("ok repeating")
    elif "yes" in speech:
        speak("ending loop now")
        break
    else:
        speak("Unrecognizable repeating")