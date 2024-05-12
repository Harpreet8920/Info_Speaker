import wikipedia
import pyttsx3

voice = pyttsx3.init()
In = input("Searching in Wikipedia/Google: ")
result = wikipedia.summary(In, sentences=3)
print(result)
voice.say(result)
voice.runAndWait()
