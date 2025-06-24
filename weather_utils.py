import os
from groq import Groq
import requests 
from api_keys import WEATHER_API_KEY, GROQ_API_KEY

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&aqi=no"

    try:
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()

        current=data["current"]
        location=data["location"]

        weather_info={
            "city":location["name"],
            "country":location["country"],
            "last_updated":current["last_updated"],
            "icon":"https:"+ current["condition"]["icon"],
            "temp_c":current["temp_c"],
            "temp_f":current["temp_f"],
            "wind_kph":current["wind_kph"],
            "humidity":current["humidity"],
            "cloud":current["cloud"],
            "feelslike_c":current["feelslike_c"],
            "feelslike_f":current["feelslike_f"],
        }
        return  weather_info 
    except Exception as e:
        print("Error fetching weather "+str(e))
        return None
        
def get_weather_joke(weather_info):
    prompt = (
        f"Give me a short, one-line funny joke or meme caption about the weather in {weather_info['city']}, {weather_info['country']}.\n"
        f"It's {weather_info['temp_c']}°C and feels like {weather_info['feelslike_c']}°C. "
        f"Conditions are {weather_info['cloud']}% cloudy with humidity {weather_info['humidity']}%."
    )

    try:
        client = Groq(api_key=GROQ_API_KEY)

        chat_completion = client.chat.completions.create(
            model="llama3-70b-8192",  
            messages=[
                {"role": "system", "content": "You're a witty weather joke generator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return chat_completion.choices[0].message.content.strip()

    except Exception as e:
        print("Error fetching joke:", e)
        return "Skies are cloudy, but my humor server is down!"