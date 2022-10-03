import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # print(voices[1].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Jarvis, Please tell me how may I help you")
# Takes microphone input from the user and returns string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")  
        r.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query= r.recognize_google(audio,language='en-in')
        print(f"User Said:{query}\n")
    except Exception as e:
        print("Say that again please...")
        return "NONE"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('xyz@gmail.com','your password')
    server.sendmail('xyz@gmail.com',to,content)
    server.close
if __name__ == "__main__":
    wishMe()
    While=True
    query=takeCommand().lower()
    

    # Logic for executing tasks based on query.
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube'in query:
        webbrowser.open("youtube.com")
    
    elif 'open google'in query:
        webbrowser.open("google.com")

    elif 'open linkedin'in query:
        webbrowser.open("linkedin.com")

    elif 'play music' in query:
        music_dir='D:\\PRATIK\\Music'
        songs=os.listdir(music_dir)
        randNo = random.randint(0,len(songs)-1)
        os.startfile(os.path.join(music_dir,songs[randNo]))
    elif 'time' in query:
        Time=datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir the time is {Time}")
    elif 'code' in query:
        codepath='C:\\Users\\Pratik Sonawane\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
        os.startfile(codepath)
    elif 'brave' in query:
        brave='C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
        os.startfile(brave)
    elif 'chrome' in query:
        chrome='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        os.startfile(chrome)
    elif 'email to pratik' in query:
        try:
            speak("What should I Say?")
            content=takeCommand()
            to= "psonawane2252@gmail.com" 
            sendEmail(to,content)
            speak("Email has been sent!")
        except Exception as e:
            speak("Sorry sir I am not able to send email")