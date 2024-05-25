
import pyttsx3
import pyautogui
import psutil
import pyjokes
import speech_recognition as sr
import json
import requests
import geocoder
from difflib import get_close_matches

from vosk import Model, KaldiRecognizer
import pyaudio

USE_VOSK=1
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
g = geocoder.ip('me')
data = json.load(open('data.json'))
mic = sr.Microphone()
"""for i, microphone_name in enumerate(sr.Microphone.list_microphone_names()):
    #print(microphone_name)
    if microphone_name == "External Microphone (2- Realtek(R) Audio)":
        mic = sr.Microphone(device_index=i)"""


if USE_VOSK == 1:
    model = Model(r"C:\\Users\\naveenkumar\\Downloads\\vosk-model-small-en-us-0.15")
    recognizer = KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio()
    

def recognise_vosk() -> str:
    output = 'None'
    try:    
        stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        stream.start_stream()
        while True:
            data = stream.read(4096)
            if recognizer.AcceptWaveform(data):
                text = recognizer.Result()
                output = text[14:-3]
                break
        mic.close()
    except Exception as e:
        print('Say that again please...')
    return output

def speak(audio) -> None:
        engine.say(audio)
        engine.runAndWait()

def screenshot() -> None:
    img = pyautogui.screenshot()
    img.save('path of folder you want to save/screenshot.png')

def cpu() -> None:
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def joke() -> None:
    for i in range(5):
        speak(pyjokes.get_jokes()[i])

def takeCommand() -> str:
    if USE_VOSK == 0:
        r = sr.Recognizer()
        with mic as source:
            
            print('Listening...')
            r.pause_threshold = 1
            r.energy_threshold = 494
            r.adjust_for_ambient_noise(source, duration=2)
            audio = r.listen(source)
            

        try:
            print('Recognizing..')
            query = r.recognize_google(audio, language='en-in')
            print(f'User said: {query}\n')

        except Exception as e:
            # print(e)

            print('Say that again please...')
            return 'None'
    else:
        query = recognise_vosk()
    print('query:'+query)
    return query


def weather():
    # https://api.open-meteo.com/v1/forecast?latitude=10.7860267&longitude=79.1381497&current=temperature_2m&hourly=temperature_2m
    api_url = "https://api.open-meteo.com/v1/forecast?latitude=" + \
        str(g.latlng[0]) + "&longitude=" + str(g.latlng[1])+"&current=temperature_2m"

    data = requests.get(api_url)
    data_json = data.json()
    if data_json['current'] != None:
        value = data_json['current']['temperature_2m']
        speak('Temperature:'+str(value)+" degree celcius")


def translate(word):
    word = word.lower()
    if word in data:
        speak(data[word])
    elif len(get_close_matches(word, data.keys())) > 0:
        x = get_close_matches(word, data.keys())[0]
        speak('Did you mean ' + x +
              ' instead,  respond with Yes or No.')
        ans = takeCommand().lower()
        if 'yes' in ans:
            speak(data[x])
        elif 'no' in ans:
            speak("Word doesn't exist. Please make sure you spelled it correctly.")
        else:
            speak("We didn't understand your entry.")

    else:
        speak("Word doesn't exist. Please double check it.")
