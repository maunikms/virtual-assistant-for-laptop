import speech_recognition as sr

def takeCommand():
    #it take input from the user and return output in string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
		# r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n" )

    except Exception as e:
        # print(e)
        print("Say that again please...")
        # speak("Say that again please...")
        return "None"
    return query
