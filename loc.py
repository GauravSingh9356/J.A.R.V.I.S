# I have made changes to this file as geocoder is not functioning well
import requests
import json
import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def weather():
    api_key = "give-your-api-key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?" #Now Taking weather data from openweather.org
    
    speak("Tell me the name of the city")

    city_name = takeCommand()
    speak("Please Wait ...")

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
 
    response = requests.get(complete_url) 
 
    x = response.json() 

    if x["cod"] != "404": 
 
	    y = x["main"] 
 
	    current_temperature = y["temp"] 

	    current_pressure = y["pressure"] 

	    current_humidiy = y["humidity"] 
 
	    z = x["weather"] 

	    minimum_temperature = y["temp_min"]
 
	    weather_description = z[0]["description"] 
 
	    speak(" Temperature (in kelvin unit)  " +
					str(current_temperature) +
		    "\n atmospheric pressure (in hPa unit)  " +
					str(current_pressure) +
		    "\n humidity (in percentage)  " +
					str(current_humidiy) +
		    "\n minimum temperature (in percentage)  " +
					str(minimum_temperature) +
		    "\n description " +
					str(weather_description)) 

    else: 
	    speak(" City Not Found ") 

if __name__ == '__main__':
    weather()
    
  # Happy Coding
