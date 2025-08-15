import pyttsx3
import speech_recognition as sr #Library for converting speech into text using different APIs (here we’re using Google’s free speech API).

def get():
    r = sr.Recognizer()  #Opens your system’s default microphone as an audio source.
    with sr.Microphone() as source: #The with statement automatically closes the microphone after recording.
        print("Say Something Please.!")
        audio = r.listen(source) #Listens to the audio until you stop speaking (detects silence).
        print("Done")

    try:
        text = r.recognize_google(audio) #Sends the recorded audio to Google’s speech recognition service.
        print('You Said please '+text)

    except Exception as e:
        print(e)

get()                