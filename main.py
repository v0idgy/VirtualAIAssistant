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
            session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..ItgvFWSJdJ5cOFGp.ly8eQl41a2VZSrJty5slrxaaOTiW00DYLFVKckiOvEH7YTVp1gnZLRY8yTkHgSH9K3quJJ2CuKC1XleOyi5tbj4XXtb1puRaU7zt24XdWtEQMN-f_gTMreGfyXorg7wu3elXibPDcXvE16BrJ80x1neluh7IQq3GHBm838J10YltC8mNZ_S2fLzPw5RMREnFl9pu2MkE3odB-KtsFkRDTnUGxjbmdjkfHVxiF7-NWiYicYr0NgE9u2Ooz2ktWzMyZQmuq6IDY-IOU7JZ8gu3It7MharIQcPIoJLIK2mh7P1Xu4RF5gjXfYh_fkhS8Tpf0Efj1NeKffRGNx7WSuyqZArHKr-D13F4heAU03m_nexbq10fTWz2nV0R-yLGq8q_ubtkCebdcidM35ZOPzZmEWfA160wXFp157aw9TZOkymRgRnE3kHE5Z6-vEvoLT9deXJ4E9BneD-1LxREqX6T7zhC8o4GXyi6I37TqSVt_Qv_brr5H7g_XGIUFl_UQEIQ2KRnPq_o33dWjJo0u7Wd5YB_4GR-iDZKCUKdGMGjnzRZUInS8iBp71gR6d_EAx7UF2aNJDKSSDdI2HZKf_Quj612Zl0277PDciMpDjHZLP0QMkWbkYuN2JqXMaVwzwvP9bzpEoqISk-AWGVKCQi2nw7gRiWfUf35xFN4-nZECRp26DZNQKJ14FoNWeHlFbB3UXG0fZqp6jvuKL1OU8-0sqpNcHOhXPVPcRxstWKQ0zcR8HbFO7U8XE1a8Ploq1hGblnknEKSJ79bxk6BGu_-Iml5mHurvDpc_cIj-yHHokbLummIC7MB6GwSg7iClqqmYJk0q-JrL1klK4FKKFvIU1WCSnzUVNw4sd3z7hvnH_L-evhVspOSWHkUMrsPiB8OoTQglqNx371lEjzPJHDrGsmhpH-zW_rBngrEsoI6Odn5tcP6mEUPBWZ27Nxl2GiB3HHOoisKdGpvzPfPi34DL6qYgbJtVEtkspH7EZdpt-sfA-OYeL9oonN8rNUQn787PHLHly0zpMBK5_CMHBeIaihVPmhyhkZuWuL9MhSVHPrsC36I5J2MwSmHSJbKysYonozb1vN6YHvaOCy64DuXNqJ8ulZ6JGR9TJ6isshWWm37jV9I6xw3Hz6i2JtCLITmsBPrUamhB6x9WwALZgn_UGnNq-m2yOV9sKbHVXkq1807K_3KF25AEg-jJSJY7KfU358Or7giVXIsg_ihzYzGrYSsY7mTG3mCMcpqP8UqnJKVk6uLBM3MC_JxAV-1DLkJN6yr9KLukSHt0-rtO6_rQ9Ji9WrGFmYwYNuS5K9mF06OK3Xbe_xyinlhEo3d8BSJgF1k7LteZGL89I8LZawH68VELl5AvK2yzMBoRKih2UII3Leb25gc-48MGohO7er1UWw1oxaFWXJeuUjaI-6QO80UPM_8xH5d9lVTfq0URrxoPpn0QN2C7QXh50ImntzDzAqRQ5Hcaac0vHxqyJC0HmGPEBlqu1YOTu38XTMUXEk7bvT_UHwuOid0VISW9fcNJ-sdEFqa8YyBrD994Qtdn0bFONj3aR8gm3rPMPKgyPXXQzI_8cwVf37SwFgisNItIAk7y6IKA4IBOjmFogj-kDMS4e5EYbN6SxUSlan1eYTVBL3-X_oqMHmTZUSn6G8SuBey4rLe-eoTXFDTA5-9QtPZeTnjZEg2pFDgadF-v_8ztpGqV9lNufWxhscucwXGaNKVA1uaOsJ1NlVPm4AsaXIW97n0OGu6YGFz8dL7gIWSMbo8H4dy4n0t5d-ZicO4iUOcBQm_py6R4Sbi4AsqxfZnQ95AKlmNTo3AZ5Tb-znQpZ8c8KF5-izeoY6786tb1XS-_VH2jHuai4PEJ1PIB52_eMoNpibKMRwmGoD6_ZPO5roW592oL3WcD0jIiPVPiQSeXXgiO6pU18LxsXJeIx3H3T8bUVsg7eSz95SL7VKp_HHugM5ii97EvfD30g4i05Ih_Ex7Fv9gyoAcf2pT9FUtaaLKzuPx78e7YUn2CoFJQHYfgzecvytlaDxc8mmr8Fqp8mZkt9DynvQVuLEQdVvs3EUEwbGmju8BLZJtzPaOuRl43Hj2xfLHOWGFhDzhrap-A4fzKgw8O6Ige-CQFePFNrSmKarXTazIQKhf-wO4DAQVRYuoBfJNNua9e_B7a2_tMu1r7H2DorT1ZIjcCKhyVzu88-wsdKROCv7fwZMBMpSdDGK8Mcp8YHx9ZMjIUjzpWeTc1dNovihIp8wo_2J9DAFn9rkRH3Vu76zB1-SIyQ.ajHIX4UkfnrDMAJTfjv7zQ'  # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
            api = ChatGPT(session_token)
            speak("what is your query for chat gpt")
            query=takeCommand()
            resp = api.send_message(query)
            
            print(resp['message'])
            speak(resp['message'])
            time.sleep(5)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
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
                  'opening youtube, google chrome, gmail and stackoverflow ,predict time ,search wikipedia,predict weather ' 
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


