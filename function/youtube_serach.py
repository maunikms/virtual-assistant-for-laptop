import speech_recognition as sr
import webbrowser

def youtube_serach(topic):
    sr.Microphone(device_index=1)

    r=sr.Recognizer()

    with sr.Microphone() as source:
        
        try:
            text=topic
            print("You said : {}".format(text))
            url='https://www.youtube.com/results?search_query='
            search_url=url+text
            webbrowser.open(search_url)
        except:
            print("Can't recognize")