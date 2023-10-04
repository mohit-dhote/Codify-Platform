import speech_recognition as sr
import datetime
import webbrowser as wb
import os
import pyttsx3
import wikipedia
import pywhatkit
import pyjokes as pj
import smtplib
import requests
from bs4 import BeautifulSoup
import winsound
import operator
import random
import pyttsx3



# from decorator import tick_tock

engine = pyttsx3.init()



def sendmail():
    receivers = ['avyay.jain2001@gmail.com', 'rajatthakurk@gmail.com', 'aryanverma2612001@gmail.com']
    a = smtplib.SMTP('smtp.gmail.com', 587)
    a.starttls()
    a.login('avyay.jain2001@gmail.com', 'PintooAvyay_11')
    a.sendmail('avyay.jain2001@gmail.com', receivers, 'test message')
    a.quit()


def search():
    speech("enter the topic you want to search on wikipedia  ")
    query = takeCommand().lower()
    wresult = str(wikipedia.search(query, results=1))
    results = wikipedia.summary(wresult, sentences=2)
    speech("According to Wikipedia")
    print(results)
    speech(results)


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        wish = 'good morning'
        # speech('good morning')
        # print('good morning')
    elif 12 <= hour <= 18:
        wish = 'good afternoon'
        # speech('good afternoon')
        # print('good afternoon')
    else:
        wish = 'good evening'
        # speech('good evening')
        # print('good evening')

    return wish


def Whatsapp():
    speech('opening whatsApp')
    os.startfile('C:\\Users\\avyay\\AppData\\Local\\WhatsApp\\WhatsApp.exe')


def chrome():
    speech('opening chrome')
    os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')


def speech(audio):
    engine.setProperty('rate', 175)
    voices = engine.getProperty('voices')  # getting details of current voice
    # engine.setProperty('voice', voices[1].id)  # changing index, changes voices. o for male
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def dateAndTime():
    time = datetime.datetime.now().strftime("%Y\n %B\n %A\n %I %M %S %Z")
    print(time)
    speech(time)


def google():
    wb.open('google.com')
    speech("opening google")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print()
        print("Listening...")
        print()
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        print()
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        print()
        print(e)
        return "None"
    return query


def playmusic():
    speech("what would you like to play ")
    song = takeCommand()
    speech('playing ' + song)
    pywhatkit.playonyt(song)


def joke():
    speech('telling a joke')
    a = pj.get_joke(language='en', category='neutral')
    speech(a)
    print(a)


def searchOnGoogle():
    speech('what would you like to search on google')
    print('what would you like to search on google')
    a = takeCommand()
    pywhatkit.search(a)


def weather():
    speech("please tell city name ")

    city = takeCommand().lower()
    print(city)

    url = "https://google.com/search?q=" + "weather" + city
    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')

    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    time_skyDescription = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    data = time_skyDescription.split('\n')
    time = data[0]
    sky = data[1]

    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

    strd = listdiv[5].text

    pos = strd.find('wind')
    otherData = strd[pos:]

    print("Temperature is ", temp)
    speech("Temperature is " + temp)
    print("time is ", time)
    speech("time is " + time)
    print("sky description: ", sky)
    speech("sky description: " + sky)
    print(otherData)


def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing, "%I:%M %p"))

    altime = altime[11:-3]
    print(altime)
    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)

    print(f"Done, alarm is set for {Timing}")

    while True:
        if Horeal == datetime.datetime.now().hour and Mireal == datetime.datetime.now().minute:
            print("alarm is running")
            winsound.PlaySound('abc', winsound.SND_LOOP)

        elif Mireal < datetime.datetime.now().minute:
            break


def calculate():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speech("say what you want to calculate, example 3 plus 3")
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        my_string = r.recognize_google(audio)
        print(my_string)

        def get_operator_fn(op):
            return {
                '+': operator.add,
                '-': operator.sub,
                '*': operator.mul,
                'divided': operator.__truediv__,
            }[op]

        def evel_binary(op1, oper, op2):
            op1, op2 = int(op1), int(op2)
            return get_operator_fn(oper)(op1, op2)

        speech("your result is ")
        speech(evel_binary(*(my_string.split())))


def coin():
    a = random.randint(0, 1)

    if a == 0:
        speech("the coin says its tail")
        print("the coin says its tail")
    else:
        speech("the coin says its heads")
        print("the coin says its heads")


def die():
    a = random.randint(0, 5)

    if a == 0:
        speech("the die says its 1")
        print("the die says its 1")
    elif a == 1:
        speech("the die says its 2")
        print("the die says its 2")

    elif a == 2:
        speech("the die says its 3")
        print("the die says its 3")

    elif a == 3:
        speech("the die says its 4")
        print("the die says its 4")

    elif a == 4:
        speech("the die says its 5")
        print("the die says its 5")

    else:
        speech("the die says its 6")
        print("the die says its 6")


wish = wishMe()
print(wish)
speech(f"{wish} sir, i am jarvis what would you like to do")

while True:

    speechInput = takeCommand().lower()
    # print(speechInput)

    if 'time' in speechInput:
        dateAndTime()

    elif 'google' in speechInput:
        google()

    elif 'play music' in speechInput:
        playmusic()

    elif 'open whatsapp' in speechInput:
        Whatsapp()

    elif 'open chrome' in speechInput:
        chrome()

    elif 'search' in speechInput:  # wikipedia
        search()

    elif 'tell me a joke' in speechInput:
        joke()

    elif 'send mail' in speechInput:
        sendmail()

    elif 'exit' in speechInput:
        speech("goodbye sir going off duty")
        print("goodbye sir going off duty")
        exit()

    elif 'search on web' in speechInput:
        searchOnGoogle()

    elif 'weather' in speechInput:
        weather()

    elif 'what is your name' in speechInput:
        speech('my name is jarvis your personal voice assistant')

    elif 'who made you' in speechInput:
        speech('i was made by avyay jain')

    elif 'what is my name' in speechInput:
        speech('my name is avyay jain')

    # elif 'f*** you' in speechInput:
    # speech('bhosdike ek kantap lagaenge sari fuck wak wali backchodi chali jaegi')

    elif 'alarm' in speechInput:
        speech("say set alarm for 5:30 am ")
        print("say set alarm for 5:30 am")
        tt = takeCommand()
        tt = tt.replace("set alarm to ", "")
        tt = tt.replace(".", "")
        tt = tt.upper()
        alarm(tt)

    elif 'calculate' in speechInput:
        calculate()

    elif 'coin' in speechInput:
        coin()

    elif 'dice' in speechInput:
        die()

def adjust_voice_tone_and_pacing(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Adjust the voice properties (you can experiment with these values)
    rate = engine.getProperty('rate')  # Speed of speech
    volume = engine.getProperty('volume')  # Volume (0.0 to 1.0)
    
    # Increase the rate (higher value makes it faster, e.g., 200)
    engine.setProperty('rate', rate + 50)
    
    # Decrease the volume (lower value makes it quieter, e.g., 0.5)
    engine.setProperty('volume', volume - 0.1)
    
    # Speak the text with adjusted tone and pacing
    engine.say(text)
    engine.runAndWait()

# Example usage:
adjusted_text = "This is an example of adjusted voice tone and pacing."
adjust_voice_tone_and_pacing(adjusted_text) 


    elif "search" in named_entities:
        search()
    # ... Add more intent-based logic here

    # Default behavior if no specific intent is recognized
    else:
        speech("I'm sorry, I didn't understand that command. Can you please repeat or rephrase?")



