import speech_recognition as sr


r = sr.Recognizer

with sr.Microphone() as source:
    print("Lütfen bir Şey Söyleyin.")
    audio = r.listen(source)
    print("Zamanınız doldu. Teşekkürler!")

try:
    print("TEXT: "+r.recognize_google(audio));
except:
    pass;