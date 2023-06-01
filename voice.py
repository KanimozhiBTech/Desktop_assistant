import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os 

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir")
    else: 
        speak("Good evening sir")
    speak("what can i do for u sir")

def takecommand():
     r=sr.Recognizer()
     with sr.Microphone() as source:
         print("listening....")
         r.pause_threshold=1
         r.adjust_for_ambient_noise(source,duration= 1)
         audio=r.listen(source)
     try:
         print("wait for few minutes")
         query=r.recognize_google(audio,language='en-in')
         print("user said",query)
     except Exception as e:
         print(e)
         speak("speak that again please")
         query="nothing"
     return query






if __name__ == "__main__":
    wishme()
    while True:
        query=takecommand().lower()
        if "wake up" in query:
            speak("i am ready sir")
    #speak("kani is very good girl")
            while True:
                query=takecommand().lower()
        #logic for executing tasks based on query
                if "wikipedia" in query:
                    speak("searching in wikipedia")
                    query=query.replace("wikipedia","")
                    results=wikipedia.summary(query,sentences=2)
                    speak("According to wikipedia")
                    print(results)
                    speak(results)

                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")
                elif 'open google' in query:
                    webbrowser.open("google.com")
                elif 'open chrome' in query:
                    webbrowser.open("chrome.com")
                elif'play music' in query:
                    musicdir="D:\\songs"
                    songs=os.listdir(musicdir)
                    print(songs)
                    os.startfile(os.path.join(musicdir,songs[4]))
                elif'open code' in query:
                    codepath="F:\\Microsoft VS Code\\Code.exe"
                    os.startfile(codepath)
                elif'the time' in query:
                    time=datetime.datetime.now().strftime("%H:%M:%S")
                    speak(time)
                
