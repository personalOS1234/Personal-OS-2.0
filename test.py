import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('time')
    audio = r.listen(source)

try:
    print(r.recognize_google(audio))

except Exception as e:
    print(e)
