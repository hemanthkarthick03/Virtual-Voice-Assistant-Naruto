''' Vitrual Voice Assistant By Hemanth Karthick '''
# Libraries
import mysql.connector
import speech_recognition as sr
import pyttsx3
import datetime
import time
import subprocess
import wolframalpha
import requests
import json
import spotipy
import webbrowser
import platform
import random
import pygetwindow as gw
import PyDictionary as dic
import wikipedia
import screen_brightness_control as sbc
import cv2
import mediapipe as mp
from bs4 import BeautifulSoup
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice','voice[0].id')
newVoiceRate=160
engine.setProperty('rate',newVoiceRate)

def speak(text):
    engine.say(text)
    engine.runAndWait()
                
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=5 and hour<12:
         print("\n\t\t\t\t\t\tHello 👋  Good Morning Buddy\n")
         print("-------------------------------------------------------------------------------------")    
         speak("Hello Hamanth Karthick, Good Morning Buddy")
       
    elif hour>=12 and hour<15:
        print("\n\t\t\t\t\t\t\tHello 👋 Good Afternoon Homie\n")
        print("--------------------------------------------------------------------------------------")    
        speak("Hello Good Afternoon Homie")
    
    elif hour>=15 and hour<20:
        print("\n\t\t\t\t\t\t\tHello 👋 Good Evening Homie\n")
        print("--------------------------------------------------------------------------------------")    
        speak("Hello Good Evening Homie")
    
    else:
        print("\n\t\t\t\t\t\t\tHello 👋 Homie\n")
        print("--------------------------------------------------------------------------------------")    
        speak("Hello Homie")
        


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤  🎙  Hearing  🎙  🎤\n")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"Hemanth Karthick 😎 ~ {statement}\n")

        except Exception:
            print("[# Microphone Error] ---  Sorry 😅 ! Say that again please !!!\n")
            print("-------------------------------------------------------------------------------------")
            speak("Pardon me, please say that again")
            return "None"
        return statement

print("-------------------------------------------------------------------------------------")    
print("\n\t                  Loading your Virtual Assistant - Naruto                      \n")
print("-------------------------------------------------------------------------------------")    
print('''                                                                          
                                                                                          
                                .:.               .:^:                                    
                                .~:^:.         .:::. ^.                                   
                                 ~. .:^:.   .:^:      :                                   
                     .:..        ^.    .:^:^:.        .^  .....:::~                       
                     .~..::::::. ^:       .            :::....   .^                       
                      ~.      ...:.                              ^:                       
                      :^                                         ~.                       
                       ~:                                        ...:::::.....            
            :^:....::::^^                                                ..:~.            
            .^^.                                                          ::              
              .^^.                                                      .^:               
                .^:               :.......::::.......                  .^.                
                 .~.             :~:................::::::~.            .::.              
               .^:               ^       ............     .^.             .::.            
             :^:         ::     ^^.:.:............::::::::::!.          .   .::.          
            ^^:... .:   :^^    .:            .......        .^:    .   .^ ....:~:         
               ...:~.  :: ^.  .~.          .^......         ::^:   ~^.  ~^:....           
                   ^  ::  .^ .^:.         :^^.::^.          :. ^: .^.^: ::                
                  .^ ::    ^.!.:.        ^^:~:.::.         .^  ^~::^  :^:~                
                  ::::     .~~:.:        .......           .^ .^ ^~:   .!!.               
                  :~~         ^..::^^^^^^^^^^^^^^^^^^^^^^^^^^^~.  :    ::..               
                  ..^.         ...............  ..     .......         ~.                 
                    :^..:::::::.::^^^^~~^::::::::::.:^~!~^~^:.::::^::.^~                  
                    .~~..~    .!7??7~^:~!^         :!!!7???7!~^   ^^.:!:^^                
                   :::~ .^   .Y?~!!~!7~          . ...~!7^~^~^57  :: ~...~.               
                   ^^:!:.~    ~.^~7~~^.        .~.    .^!~7~!.^.  :^.~:7:^.               
                   :..7?!~      :^^^^:.        ::     .:^~~~:     :77^~::~                
                   .:~!:~!                                        .^^:?::^                
                    .^!^^:...::.                            .:::::.^^!!:~.                
                     ::::^:....                                  .:~!~:~.                 
                     .:..~.    ..                                 ^.::^.                  
                        .~:.::::.           ::   ::         .:::.^~:::                    
                         :^:.                                   :^~.                      
                          ^.:  .::                          .. :^.:                       
                          :..:::.    .:::::::::::::.::::    .:~^ ^.                       
                          .^^::^.                           :^~::^                        
                           :.:^~.::.                     .:^..7~~:                        
                             :~!...::.                 .:^.  .!:::                        
                             ^ ...^..:::.           .::^:. ^::. ::                        
                            .:    ....::^^...  ...::~^^^::::    :^                        
                            ::       .   ...:~^....           : .~                        
                            ^::. .   .   .  :!^            .  :  ~.                       
                            ^.:. .   :   .  .~:     ..  .. .  .  :~.                      
                          .:!..  .   . . .  .~.  :  ..  .:      :^^:::.                   
                       .:.. .:^.       .    .~:  .   .   .   ..::                         
                               ::^:.::.     .~:      .   .:..:.                           
                                    ..::::..:^:..::.:::.....                              
                                         ....  .....                                      


@@@@@@@@@@@@@&7Y@@@@@@@&B&@@@@@&&##&@@@@@@@@@@@@@@@@@@@@&&BG5Y?7!~^^^~!?5#@@@@@@@@@@@
@@@@B#&#&&@@@?YY?B@@&55J?JYG@BYY???JYYPG#@@@&#&@@@#G5JJJ7.    .....      .J&@@@@@@@@@
@@@5?JJ??J?5?Y~.5!JYJJ~: ^BJ:7J:    .:~7?YP5?JJY!^^:.J!^?J?7!!!!!!!J^ ^!7!!JYY5G&@@@@
@@P?J .  !5.5^  Y7 5!     ~P:5^   ^~:    ~YJJ .~Y:!^5~  .#~        .P57:.:: .:!?JP@@@
@@7P:    P^7J   P::5.      ~Y5^   5BY.    !@^   5~ ~5   !G::^.   .?7#7    ..    ?J7&@
@@!5.    7J?J  .P^P:  .!.  ^YJ!  .~:    .!YB:   5~ P^   YJ!~P!   7Y!5   ^J!??    G.:B
@B!J      7#~  ^G5~   ~5.  .55!      :~?7~:P.  .P 7J   :P   J7   5?5.  .P:  G:  .P. ?
@JJ~       !.  !G:          P~     :55~    P:  .G^P.   Y!   5~  ^GP.   ^5  !5   ??  ?
@!P.  ~P.      Y~   :7?5.  ~#5.     .~77^  Y~   ?5^   .P.  .P.  7JY!   ~P:?J.  7Y   G
G7J  .575:    .#~  ^P^.G.  JYP   !~.   .~7~YJ         ^P  !~P   Y!~5   .?!:  .JJ   Y@
?5^  ?J ~Y~.::5P   P~  P^ ~575: ~P!?7~:   .~Y?~. ^~   !P. P75^ .P~ J7.    .^7J~   Y@@
Y??~J7.  ?!?!~!?7!J?  :7YJ?. :7??.  .^!77~.. :!JP?J?!?!.  JG7J7?~  .?777777!:   ~G@@@
@P7^.  .!!    . ...  .BG:^     .  .^~~. .~!!77~^~P!..   :J@@@J.   ^P#7.      ^7G@@@@@
@@&?.!5J:  ^PBJ     .?##GJ:.77!!^ .^^^~!?5!:..:^^~   ?YP&@@@@@B5?G@@@@#GPPPG#@@@@@@@@
@@@@&@?    B@@J         ....::^^~!7!!~~~Y@@&&B5?~:^^5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@?     5@@@#5J?77777????7!~^^^^!?5G&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@7      :!7JJJJ?7!~^^:^^~7J5G#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@&5!^^^^^:::::^~!?Y5G#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ''')
print('\n')
print("-------------------------------------------------------------------------------------")    
speak("Loading your Virtual Assistant Uzumaki Narutho")
wishMe()


if __name__=='__main__':


    while True:
        sentence=random.choice(["How can I help you now, mate?", 
                                 "Say what I can do for you?",
                                 "Do you want me to help you pick something?",
                                 "What can I do for you?","" ])
        speak(sentence)
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement or "end" in statement or "mood" in statement or "tata" in statement:
                print('Your Personal Assistant Naruto is Shutting down, Have a Good Day! Bye')
                print("-------------------------------------------------------------------------------------")    
                speak('Your Personal Assistant Naruto is Shutting down, Have a Good Day! Bai')
                break

        elif "wikipedia" in statement:
                speak('Searching in Wikipedia...')
                statement =statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=2)
                speak("According to Wikipedia")
                print("------------------------------------------------------------------")    
                print(results)
                print("-------------------------------------------------------------------------------------")
                speak(results)
                
        elif "thank you" in statement :
                print('Its my pleasure! Your Personal Assistant Naruto is Shutting down, Have a Good Day! Bye')
                print("-------------------------------------------------------------------------------------")    
                speak('Its my pleasure! Your Personal Assistant Naruto is Shutting down, Have a Good Day! Bai')
                break
            
        elif 'youtube' in statement:
                text="None"
                while(text=="None"):
                    print("What do you want to search now?")
                    speak("What do you want to search now?")
                    text=takeCommand()
                a=''
                L = text.split(" ")
                for i in range(0,len(L)):   
                    if i==0:
                        a=L[i]+a
                    else:    
                        a=a+'+'+L[i]
                url="https://www.youtube.com/results?search_query=" + a
                webbrowser.open_new_tab(url)
                speak("your search in youtube is open now")
                time.sleep(5)

        elif 'google' in statement or 'chrome' in statement or 'search' in statement:
                text="None"
                while(text=="None"):
                    print("What do you want to search now?")
                    speak("What do you want to search now?")
                    text=takeCommand()
                url="https://www.google.co.in/search?q=" + text
                webbrowser.open_new_tab(url)
                speak("Your search in Google Chrome open now")
                time.sleep(5)

        elif 'gmail' in statement or 'mail' in statement:
                webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
                speak("Google Mail open now")
                print("\n-----------------------------------------------------------------------------------")    

                time.sleep(5)
                          
        elif 'time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                print(f"The time is {strTime}\n")
                print("-------------------------------------------------------------------------------------")    
                speak(f"the time is {strTime}")
                
        elif 'date' in statement or 'day' in statement:
                now = datetime.datetime.now()
                dt_string = now.strftime("%B %d %Y")
                print("Date =", dt_string)	
                print("-------------------------------------------------------------------------------------")    
                speak(dt_string)	
        
        elif 'news' in statement:
                '''news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India, Happy reading')
                time.sleep(6)'''
                url = 'https://www.bbc.com/news'
                response = requests.get(url)
  
                soup = BeautifulSoup(response.text, 'html.parser')
                headlines = soup.find('body').find_all('h3')
                for x in headlines:
                    print(x.text.strip())
                    speak(x.text.strip())

        elif "camera" in statement or "take a photo" in statement:
                vid = cv2.VideoCapture(0)
                while(True):
                    ret, frame = vid.read()
                    cv2.imshow('frame', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                vid.release()
                cv2.destroyAllWindows()
                
        elif "music" in statement or "song" in statement:
                text="None"
                username = 'edip82mzzgfwr0a6y7mroun60'
                clientID = '90b522c3a3fe4403b01933b5e1c6c98a'
                clientSecret = '7b609f8f1e4f40c5877310a2c03cb100'
                redirectURI = 'http://google.com/'

                oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
                token_dict = oauth_object.get_cached_token()
                token = token_dict['access_token']
                spotifyObject = spotipy.Spotify(auth=token)
                user = spotifyObject.current_user()
                # To print the response in readable format.

                oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
                token_dict = oauth_object.get_cached_token()
                token = token_dict['access_token']
                spotifyObject = spotipy.Spotify(auth=token)
                user = spotifyObject.current_user()

                while True:
                    print("Welcome, "+ user['display_name'])
                    print("Search for a Song ")
                    print("Go to my Playlist ")
                    
                    speak("How can I help you? Search a Song or Go for a playlist")
                    choice=takeCommand().lower()
                    if (choice=="None"):
                        continue
                    elif 'search' in choice or 'find' in choice or 'song' in choice :
                        # Get the Song Name.
                        while(text=="None"):
                            print("\t\t\t\t\tSay the Song Name !!!")
                            speak('Song name please')
                            text=takeCommand()
                            if(text=="None"):
                                continue
                        a=''
                        L = text.split(" ")
                        for i in range(0,len(L)):   
                            if i==0:
                                a=L[i]+a
                            else:    
                                a=a+' '+L[i]
                        print("Song Name : \t",text.title())
                            
                        # Search for the Song.
                        searchResults = spotifyObject.search(a,1,0,"track")
                        # Get required data from JSON response.
                        tracks_dict = searchResults['tracks']
                        tracks_items = tracks_dict['items']
                        song = tracks_items[0]['external_urls']['spotify']
                        # Open the Song in Web Browser
                        webbrowser.open(song)
                        print('Song has opened in your browser.')
                        #break
                    elif 'playlist' in choice or 'play'in choice or 'list' in choice:
                        webbrowser.open_new_tab("https://open.spotify.com/playlist/2u7sFPmTRthV8RCsty158c?si=5a8d6cefa7734b2f")
                        break
                    else:
                        print("Enter valid choice !\n")
                        continue
            
            
                
                print("\n🎵 🎸 Enjoy your music 🥁 🎧\n")
                print("-------------------------------------------------------------------------------------")    
                time.sleep(10)
                
        elif 'ask' in statement:
                speak('I can answer to computational and geographical questions  and what question do you want to ask me now')
                question=takeCommand()
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                print(answer)
                speak(answer)
                
        elif 'naruto' in statement:
            print("Yeah Hemanth !")
            speak("Yeah Hamenth !")
             
        elif "who are you" in statement:
            print("I am Naruto, Your Personal Voice Assistant")
            speak("I am Uzumaki Narutho, Your Personal Voice Assistant")
            
        elif 'joke' in statement:
            pun = random.choice(["Why Couldn't The Bike Stand on it's own? It was Two Tired!", 
                                 "Whoever Stole My Copy of Microsoft Office is in Big Trouble! You got my word!",
                                 "Do you know the phrase “One man’s trash is another man’s treasure”? Wonderful saying, horrible way to find out that you were adopted.", 
                                 " It’s important to establish a good vocabulary. If I had known the difference between the words “antidote” and “anecdote,” one of my best friends would still be alive!", 
                                 "The doctor gave me one year to live, so I shot him with my gun. The judge gave me 15 years. Problem solved.",
                                 "Dark humor is like food. Not everyone gets it."])
            print(pun)
            speak(pun)
            
        elif 'version' in statement or 'system' in statement or ' operating system' in statement :
            print(platform.system())
            speak(platform.system())
            print(platform.release())
            speak(platform.release())
            print(platform.version())
            speak(platform.version())
        
        elif 'maximize' in statement or 'maximise' in statement:
            speak("Please tell the Name of the window")
            win=takeCommand().lower()
            if 'google' in win or 'chrome' in win:
                #d=webbrowser.title()
                #print (d)
                win='New Tab - Google Chrome'
            elif 'media' in win or 'player' in win:
                win='Windows Media Player'
            elif 'spider' in win:
                win='Spyder (Python 3.9)'
            elif 'notepad' in win or 'text' in win or 'document' in win:
                win='text - Notepad'
            npWindow = gw.getWindowsWithTitle(win)[0]
            npWindow.maximize()
            
        elif 'database' in statement or 'accounts' in statement or 'account' in statement or 'databases' in statement:
            win="None"
            while(win=="None"):
                    print("Please tell the Name of the table")
                    speak("Please tell the Name of the table")
                    win=takeCommand()
            
            if 'expense' in win or 'expence' in win:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="account")
                mycursor=mydb.cursor()
                mycursor.execute("SELECT * FROM expense")
                myrecords=mycursor.fetchall()
                for x in myrecords:
                     print(x)  
          
            elif 'income' in win or 'salary' in win:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="account")
                mycursor=mydb.cursor()
                mycursor.execute("SELECT * FROM income")
                myrecords=mycursor.fetchall()
                for x in myrecords:
  		             print(x)    
            
            '''elif 'savings' in win or 'saving' in win:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="account")
                mycursor=mydb.cursor()
                mycursor.execute("SELECT * FROM savings")
                myrecords=mycursor.fetchall()
                for x in myrecords:
  		             print(x)               
            '''
            
        elif 'minimize' in statement or 'minimise' in statement:
            speak("Please tell the Name of the window")
            win=takeCommand()
            if 'google' in win or 'chrome' in win:
                win='New Tab - Google Chrome'
            elif 'media' in win or 'player' in win:
                win='Windows Media Player'
            elif 'spider' in win:
                win='Spyder (Python 3.9)'
            elif 'notepad' in win or 'text' in win or 'document' in win:
                win='text - Notepad'
            npWindow = gw.getWindowsWithTitle(win)[0]
            npWindow.minimize()
            
        elif 'close' in statement :
            speak("Please tell the Name of the window")
            win=takeCommand()
            if 'google' in win or 'chrome' in win:
                win='New Tab - Google Chrome'
            elif 'media' in win or 'player' in win:
                win='Windows Media Player'
            elif 'notepad' in win or 'text' in win or 'document' in win:
                win='text - Notepad'
            elif 'project' in win:
                win='Project'
            npWindow = gw.getWindowsWithTitle(win)[0]
            npWindow.close()
            
        elif 'thesaurus' in statement or 'meaning' in statement or 'dictionary' in statement or 'synonym' in statement or 'parallel' in statement:
            speak("Say the word for which you need the synonym")
            di=dic.PyDictionary()
            word=takeCommand().lower()
            print(di.synonym(word))
            speak(di.synonym(word))
        
        elif 'opposite' in statement or 'antonym' in statement or 'anti' in statement:
            speak("Say the word for which you need the antonym")
            di=dic.PyDictionary()
            word=takeCommand().lower()
            print(di.antonym(word))
            speak(di.antonym(word))
        
        elif 'notepad' in statement or 'write' in statement or 'document' in statement:
            speak("Tell me the statements to be written on the notepad")
            print("Contents to the notepad")
            f=open("text.txt",'w')
            win=None
            while (win!='end' or win!='over' or win!='close' or win!='closure' or win!='and'):
                win=takeCommand().lower()
                if win=='end' or win=='over' or win=='close' or win=='closure' or win=='and':
                    f.close()
                    webbrowser.open_new_tab("file:///E:/Python Programs/Project/text.txt")
                    break
                if win=='none':
                    f.write('')
                else:
                    f.writelines(win) 
                
        elif "weather" in statement or "climate" in statement or 'temperature' in statement:
            api_key="90bf1d92940b4542e85a85da518e2f53"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
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
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                

        elif "volume" in statement or "sound" in statement:
            cap = cv2.VideoCapture(0)
             
            mpHands = mp.solutions.hands
            hands = mpHands.Hands()
            mpDraw = mp.solutions.drawing_utils
             
             
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
             
            volMin,volMax = volume.GetVolumeRange()[:2]
             
            while True:
                success,img = cap.read()
                imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                results = hands.process(imgRGB)
                lmList = []
               
                if results.multi_hand_landmarks:
                    for handlandmark in results.multi_hand_landmarks:
                        for id,lm in enumerate(handlandmark.landmark):
                            h,w,_ = img.shape
                            cx,cy = int(lm.x*w),int(lm.y*h)
                            lmList.append([id,cx,cy])
                        mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS)
                        
                
                if lmList != []:
                    x1,y1 = lmList[4][1],lmList[4][2]
                    x2,y2 = lmList[8][1],lmList[8][2]
             
                    cv2.circle(img,(x1,y1),4,(255,0,0),cv2.FILLED)
                    cv2.circle(img,(x2,y2),4,(255,0,0),cv2.FILLED)
                    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)
             
                    length = hypot(x2-x1,y2-y1)
             
                    vol = np.interp(length,[15,220],[volMin,volMax])
                    volume.SetMasterVolumeLevel(vol, None)
             
                    # Hand range 15 - 220
                    # Volume range -63.5 - 0.0
                    
                cv2.imshow('Image',img)
               
                if cv2.waitKey(5) == ord('q'):
                    break

            
            cv2.destroyAllWindows()  
            

        elif "bright" in statement or "brightness" in statement:
            cap = cv2.VideoCapture(0)
             
            mpHands = mp.solutions.hands
            hands = mpHands.Hands()
            mpDraw = mp.solutions.drawing_utils
             
            while True:
                success,img = cap.read()
                imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                results = hands.process(imgRGB)
             
                lmList = []
                if results.multi_hand_landmarks:
                    for handlandmark in results.multi_hand_landmarks:
                        for id,lm in enumerate(handlandmark.landmark):
                            h,w,_ = img.shape
                            cx,cy = int(lm.x*w),int(lm.y*h)
                            lmList.append([id,cx,cy])
                        mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS)
                
                if lmList != []:
                    x1,y1 = lmList[4][1],lmList[4][2]
                    x2,y2 = lmList[8][1],lmList[8][2]
             
                    cv2.circle(img,(x1,y1),4,(255,0,0),cv2.FILLED)
                    cv2.circle(img,(x2,y2),4,(255,0,0),cv2.FILLED)
                    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)
             
                    length = hypot(x2-x1,y2-y1)
             
                    bright = np.interp(length,[15,220],[0,100])
                    sbc.set_brightness(int(bright))
                    
                    # Hand range 15 - 220
                    # Brightness range 0 - 100
             
                cv2.imshow('Image',img)
                
                if cv2.waitKey(5) == ord('q'):
                    break
           
            cv2.destroyAllWindows()


        elif "log off" in statement or "sign out" in statement:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])
			
time.sleep(3)
