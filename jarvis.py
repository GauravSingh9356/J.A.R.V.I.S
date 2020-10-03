import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import datetime
import os
import sys
import smtplib
from news import speak_news, getNewsUrl
from diction import translate
from loc import weather
from youtube import you
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)

        print('Say that again please...')
        return 'None'
    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning SIR")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon SIR")

    else:
        speak('Good Evening SIR')

    weather()
    speak('I am JARVIS. Please tell me how can I help you SIR?')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email', 'password')
    server.sendmail('email', to, content)
    server.close()


if __name__ == '__main__':
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    webbrowser.register(
        'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'youtube downloader' in query:
            exec(open('youtube_downloader.py').read())

        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[1].id)
            else:
                engine.setProperty('voice', voices[0].id)
            speak("Hello Sir, I have switched my voice. How is it?")

        if 'jarvis are you there' in query:
            speak("Yes Sir, at your service")
        elif 'open youtube' in query:

            webbrowser.get('chrome').open_new_tab('https://youtube.com')

        elif 'open google' in query:
            webbrowser.get('chrome').open_new_tab('https://google.com')

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open_new_tab('https://stackoverflow.com')

      

        elif 'search youtube' in query:
            speak('What you want to search on Youtube?')
            you(takeCommand())
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strTime}')

        elif 'search' in query:
            speak('What do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get('chrome').open_new_tab(
                url)
            speak('Here is What I found for' + search)
	
	# playing random music or you can simply play music by calling its name 
	 elif 'play music' in query:
            speak("sir,which song should i play ")
            song_name=takeCommandfromUser()

            if "play random" in song_name or "random song" in song_name or "random music" in song_name:

                n=random.randint(1,11)
                music='C:\\Music\\audios'
                songs=os.listdir(music)
                print(songs)
                os.startfile(os.path.join(music,songs[n]))  #playing song

            else:
                try:
		    # put the path wher you have all the music fil
                    music_path = "C:\\Music\\audios"
                    file_search.set_root(music_path)
                    songs = file_search.searchFile(song_name)
                    # print(songs)
                    song_uri = songs[0]

                    song_in_str = ""
                    for ele in song_uri:
                        song_in_str += ele
                    print(song_in_str)
                    webbrowser.open(song_in_str)
                except Exception as e:
                    print("sir system dont have this song")

	
	
        elif 'location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)

        elif 'your master' in query:
            speak('Gaurav is my master. He created me couple of days ago')
        elif 'your name' in query:
            speak('My name is JARVIS')
        elif 'stands for' in query:
            speak('J.A.R.V.I.S stands for JUST A RATHER VERY INTELLIGENT SYSTEM')
        elif 'open code' in query:
            os.startfile(
                "C:\\Users\\gs935\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'shutdown' in query:
            os.system('shutdown /p /f')

        elif 'github' in query:
            webbrowser.get('chrome').open_new_tab(
                'https://github.com/gauravsingh9356')

        elif 'remember that' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'sleep' in query:
            sys.exit()

        elif 'dictionary' in query:
            speak('What you want to search in your intelligent dictionary?')
            translate(takeCommand())

        elif 'news' in query:
            speak('Ofcourse sir..')
            speak_news()
            speak('Do you want to read the full news...')
            test = takeCommand()
            if 'yes' in test:
                speak('Ok Sir, Opening browser...)
                webbrowser.open(getNewsUrl())
                speak('You can now read the full news from this website.')
            else:
                speak('No Problem Sir')
                      
        elif 'voice' in query:
			try:
				if 'female' in query:
					engine.setProperty('voice', voices[0].id)
				else:
					engine.setProperty('voice', voices[1].id)
				speak("Hello Sir, I have switched my voice. How is it?")
			except Exception as e:
				pass
                      
        elif 'email to gaurav' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = 'email'
                sendEmail(to, content)
                speak('Email has been sent!')

            except Exception as e:
                speak('Sorry sir, Not able to send email at the moment')
		
