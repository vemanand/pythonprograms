import speech_recognition as sr

# instance of recognizer class
r = sr.Recognizer()
print('Speak something in the microphone')
with sr.Microphone() as source:
    audio = sr.listen(source)