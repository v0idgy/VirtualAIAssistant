import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
#from ecapture import ecapture as ec
from pyChatGPT import ChatGPT
import wolframalpha
import json
import requests
import openai


print('Loading your AI personal assistant - G One')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant G-One")
wishMe()


if __name__=='__main__':

    speak("How May I Help You?")

    wake_word = 'G One'

    while True:
        

        
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant G-one is shutting down,Good bye')
            print('your personal assistant G-one is shutting down,Good bye')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            try:
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError:
                continue
        elif "g one" in statement or 'jivan' in statement:
             
            wishMe()
            speak("G-One version 1 point o in your service Sir")
            

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
        elif 'open github' in statement:
            webbrowser.open_new_tab("https://www.github.com")
            speak("github is open now")
            time.sleep(5)
        
        elif "good morning" in statement:
            speak("A warm" +statement)
            speak("How are you Mister")

        elif "where is" in statement:
            query = statement.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
            

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif "how are you" in statement:
            speak("I'm fine, glad you me that") 

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
        
        elif 'chatgpt' in statement or 'GPT' in statement or 'gpt' in statement or 'open ai' in statement:
            session_token = os.getenv("OPENAI_SESSION_TOKEN")  # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
            api = ChatGPT(str(session_token))
            speak("what is your query for chat gpt")
            query=takeCommand()
            resp = api.send_message(query)
            
            print(resp['message'])
            speak(resp['message'])
            time.sleep(5)

        elif "weather" in statement:
            api_key=os.getenv("WEATHER_API_KEY")  # Set your OpenWeather API key as an environment variable
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+str(api_key)+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif "who i am" in statement:
            speak("If you talk then definitely your human.")
        
        elif "how are you" in statement:
            speak("I'm fine, glad you me that")
 

        elif 'who are you' in statement or 'what can you do' in statement or "what's your name" in statement:
            speak('I am G-one version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube, google chrome, gmail and stackoverflow , predict time , search wikipedia, predict weather ' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!'
                  'i can also provide you information about anything available on internet using Chat GPT API ')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Gourav Yadav aka v 0 i d g y")
            print("I was built by Gourav Yadav aka v0idgy")

        elif "open stack overflow" in statement or 'open stackoverflow' in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        # elif "camera" in statement or "take a photo" in statement:
        #     ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(3)

        elif 'who is' in statement or "what is" in statement:
            # speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="63TGQT-6WVPYU4KTW"
            client = wolframalpha.Client('63TGQT-6WVPYU4KTW')
            res = client.query(question)
            try:
                answer = next(res.results).text
                speak(answer)
                print(answer)
            except StopIteration:
                print("No Results")


        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
