from weather_utils import get_weather,get_weather_joke

city=input("Enter a city: ")
weather=get_weather(city)

if weather:
    for key,value in weather.items():
        print(f"{key}:{value}")
    
    joke=get_weather_joke(weather)
    print(joke)

else: 
    print ("falied to fetch weather")



