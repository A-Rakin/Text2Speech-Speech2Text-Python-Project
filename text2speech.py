import pyttsx3 

"""
pyttsx3 is a Python Text-to-Speech (TTS) library.

It works offline and uses your system’s built-in speech engines:

Windows → SAPI5

Mac → NSSpeechSynthesizer

Linux → espeak

"""

data = input("Enter the text which you want to convert to speech:\n")

engine = pyttsx3.init()

"""
pyttsx3.init() creates a speech engine object.

This is like starting your car — before you can drive (speak), you need the engine running.

On Windows, it loads the SAPI5 speech API.
"""

engine.say(data) #This adds your text to the engine’s speech queue

engine.runAndWait()

"""

engine.runAndWait() :- This processes everything in the speech queue and plays the audio out loud.
Without this line, the program would end without saying anything.
Think of .say() as "write what to say" and .runAndWait() as "start talking".

"""