

import sre_compile
import speech_recognition as sr
from main import takeCommand
import webbrowser
from function.speak import speak

def google_serch(topic):
    
    sre_compile.Microphone(device_index=1)
   
    r=sr.Recognizer()

    with sr.Microphone() as source:
        
        try:
            text=topic
            print("You said : {}".format(text))
            url='https://www.google.co.in/search?q='
            search_url=url+text
            webbrowser.open(search_url)
        except:
            print("Can't recognize")
