
import datetime
import wikipedia
import webbrowser
import os
from function.google_search import google_serch
from function.wishme import wishMe 
from function.speak import speak
from function.takecommand import takeCommand
from function.youtube_serach import youtube_serach
from timer import * 




if __name__ == "__main__":
    wishMe() 
    while True:
        query = takeCommand().lower()

        #Logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        
        elif 'open whatsapp' in query:
        
            codePath = "C:\\Users\\sakri\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)

        elif 'close whatsapp' in query:
            import subprocess
            subprocess.call("taskkill /IM whatsapp.exe")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play song' in query:
            # music_dir = 'A:\\maunik\\e\\jarvis\\song'
            music_dir = 'A:\P P S U\jarvis\song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"mr. M S, the time is {strTime}")
        
        elif 'date' in query:
            from datetime import date
            strDate = date.today()
            speak(f"mr. M S, the today's date is {strDate}")
        
        elif "today's day" in query:
            from datetime import datetime as date

            strDay = date.today().strftime("%A")
            speak(f"mr. M S, the today's day is {strDay}")

        elif 'open vs code' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'shutdown laptop' in query:
            import os 
  
            os.system("shutdown /s /t 1") 


        elif 'google' in query:
            speak('Searching on google...')
            query = query.replace("google","")
            google_serch(query)

        elif 'youtube' in query:
            speak('Searching on youtube...')
            query = query.replace("youtube","")
            youtube_serach(query)

        elif 'close chrome' in query:
            import subprocess
            subprocess.call("taskkill /IM chrome.exe") 

        elif 'set notification' in query: 
            query = query.replace("set notification after","")
            y=int(query)*60
            countdown(y)
            