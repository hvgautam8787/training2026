from gtts import *
from playsound import playsound

text=gTTS(input("enter the text"))
text.save("a.mp3")
playsound("a.mp3")