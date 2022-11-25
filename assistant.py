import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import requests
import json
from urllib2 import urlopen 


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate',170)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("the current time is")
    speak(Time)


def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is ,")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("welcome Back LazyWizard !")
    time_()
    date_()

    #Greetings
    hour = datetime.datetime.now().hour

    if hour>=6 and hour<=12:
        speak("Good Morning ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon ")
    elif hour>=18 and hour<20:
        speak("Good Evening ")
    else:
        speak("Good Night ")
    speak("SEMI-CLONE at your service. Please tell me how can i help you today?")



def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threhold = 3
        audio = r.listen(source)
    try:
        print("Recognizing.......")
        query = r.recognize_google(audio,language='en-us')
        print(query) 
    except Exception as e :
        print(e)
        print("Say that again Please......")
        return"None"
    return query

def speak_news():
    url = 'https://newsapi.org/v2/top-headlines?language=en&category=headline&apiKey=5d07ae746a0c46bbb1aa788af81022b0'
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak("Today's Headlines are ")
    speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        speak(articles['title'])
        if index == len(arts)-1:
            break
    speak('These were the top headlines, Have a nice day Sir!!..')


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()

    server.login('username@gmail.com','password')
    server.sendmail('username@gmail.com',to,content)
    server.close()


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at '+usage)

    battery = psutil.sensors_battery()
    speak('Battery is at ')
    speak(battery.percent)


def screenshot():
    img = pyautogui.screenshot()
    img.save('D:/01 Jervis/screenshot/screenshot.png')


def love():
    speak("Ohh sir, I love you , I love you in Every universe")
    print("Ohh sir, I love you , I love you in Every universe")

def Yt_song():
        speak('Playing your favourite Song ')
        bravepath = 'YOUR PATH HERE'
       ## search = TakeCommand().lower()
        wb.get(bravepath).open_new_tab('YOUR PLAYLIST LINK HERE YOUTUBE OR SPOTIFY')

def joke():
    speak(pyjokes.get_joke())


   

if __name__ == "__main__":
    wishme()

    while True:
        query = TakeCommand().lower()

        if 'time' in query:
            time_()

        elif 'date' in query:
            date_()
    

        elif 'wiki' in query:
            speak("wait a while")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            speak('I got it ')
            #print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content=TakeCommand()
                speak("Who is the Reciever")
                reciever= input("Enter Reciever's Email:")
                to = reciever
                sendEmail(to,content)
                speak(content)
                speak("Email has been sent.")

            except Exception as e:
                print(e)
                speak("Unable to send Email.")    

        elif 'search in brave' in query:
            speak('What should I search ?')
            bravepath = 'YOUR PATH HERE'
            search = TakeCommand().lower()
            wb.get(bravepath).open_new_tab(search+'.com')

        elif "tell me about cpu" in query:
            cpu()

        elif "news" in query:
            speak_news()

        elif " joke " in query:
            joke()
            
        elif 'offline now' in query:
            speak("Going offline Sir!")
            quit()

        elif  " open telegram " in query:
            speak("Opening telegram...")
            telegram = r'YOUR PATH HERE'
            os.startfile(telegram)

        elif "Namecheap" in query:
            speak ('Opening vpn....')
            nc = r'YOUR PATH HERE'
            os.startfile(nc)

        elif "adobe reader" in query:
            speak("opening Acrobat Reader DC.... ")
            reader = r'YOUR PATH HERE'
            os.startfile(reader)

        elif "opera" in query:
            speak("opening Opera mini .....")
            opera = r'YOUR PATH HERE'
            os.startfile(opera)


       
        elif 'take a screenshot' in query:
            screenshot()
        
        elif 'love' in query:
            love()
            speak('Did you upsate Today?')
            ans = TakeCommand().lower()
            if ans  == "yes"or"true"or"yeah":
                speak('play a song for you?')
                plysng = TakeCommand().lower()
                if ans  == "yes"or"true"or"yeah":
                    Yt_song()
                else:
                    speak("Wish you would get well soon ")
            else:
                break
        

        # elif 'note' in query:
        #     speak("What should I write , Sir?")
        #     notes = TakeCommand()
        #     file = open('notes.txt','w')
        #     speak("Sir should I include Date and Time?")
        #     ans = TakeCommand()
        #     if 'yes' in ans or 'sure' in ans or 'yeha' in ans or 'ok' in ans :
        #         strTime = datetime.datetime.now().strftime("%H:%M:%S")
        #         file.write(strTime)
        #         file.write(':-')
        #         file.write(notes)
        #         speak('Done Taking Notes, SIR !')
        #     else:
        #         file.write(notes)

        # elif 'show note' or 'tell note' in query:
        #     speak('showing nots sir! ....')
        #     file = open('notes.txt','r')
        #     print(file.read())
        #     speak(file.read()) 
