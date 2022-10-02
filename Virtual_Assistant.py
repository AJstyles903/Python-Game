'''
Author : AJstyle (Mr.Aryan)
Work : Simpal And Basic Virtual Assistant 
'''
import time
import pyttsx3
import datetime
import speech_recognition as record
import webbrowser
import os
import wikipedia
import pyjokes

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')

engine.setProperty('voice', voice[0].id)

assname = 'Aryan 1 point 0'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Wish_Me():
    hour = (int(datetime.datetime.now().hour))
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !")

    speak("I Am Your Assistant.")


def username():
    
    while True:
        speak("What should i call you sir")
        uname = Take_Voice_Input()
        if uname!='None':
            break
        else:
            continue

    speak(f"Welcome Mister {uname}")

    speak("Please Tell Me How can i Help you, Sir")


def Take_Voice_Input():

    r = record.Recognizer()
    with record.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Ricognizing...")
        query = r.recognize_google(audio, language='en-in')
        # print(f"User said : {query}")
    except Exception as e:
        speak("Sorry , I don\'t understand what do you say , Say again please")
        return "None"
    return query


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    clear()
    Wish_Me()
    username()
    
    while True:

        query=Take_Voice_Input().lower()

        if 'wikipedia' in query:
            print('Serching in wikipedia...')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=1)
            print('According to wikipedia...')
            speak(result)

        elif 'open' in query:
            if('open '==query[0:5]):
                webbrowser.open(f'{query[5:]}.com')
            else:
                webbrowser.open(f'{query[:-5]}.com')

        elif 'search' in query or 'play' in query: 
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = "D:\\Music" # Your music dictionary name type in music_dir
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "don't listen" in query or 'stop' in query or "stop listening" in query:
            speak(f"for how much time you want to stop {assname} from listening commands")
            a = int(Take_Voice_Input())
            time.sleep(a)

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%I:%M:%S %p")   
            speak(f"Sir, the time is {strtime}")
        
        elif 'today' in query or 'day' in query:
            strday = datetime.datetime.now().strftime("%A")   
            speak(f"Sir, the day is {strday}")

        elif 'date' in query:
            strdate = datetime.datetime.now().strftime("%d:%B:%Y")   
            speak(f"Sir, the Date is {strdate}")

        elif 'month' in query:
            strmonth = datetime.datetime.now().strftime("%B")   
            speak(f"Sir, the Month is {strmonth}")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
    
        elif 'fine' in query or 'good' in query:
            speak("It's good to know that your fine")

        elif 'i love you' in query:
            speak("i love you 2 sir")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
    
        elif "who are you" in query:
            speak("I am your virtual assistant created by Mister Aryan")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Aryan ")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Aryan.")

        elif "what's your name" in query or "what is your name" in query:
            speak(f"My friends call me {assname}")

        elif "aryan" in query:
             
            Wish_Me()
            speak("aryan 1 point o in your service Mister")
            speak(os.uname)

        elif 'exit' in query or 'leave' in query:
            speak('Thanks for giving me your time.')
            exit()
