import pyttsx3
import speech_recognition as sr

def tts_test():
    engine = pyttsx3.init()
    engine.say("Hello. If you hear this, text-to-speech works.")
    engine.runAndWait()

def mic_test():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening for 4 seconds (speak now)...")
            audio = r.listen(source, phrase_time_limit=4)
        print("Recognizing...")
        print("You said:", r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Speech recognition service error:", e)
    except Exception as e:
        print("Microphone error:", e)

if __name__ == '__main__':
    tts_test()
    mic_test()
