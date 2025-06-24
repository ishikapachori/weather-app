# weather-app
This is a simple web app that displays the current weather for a given city along with a light-hearted joke. It uses:

- **WeatherAPI** to fetch weather information.
- **Groq (OpenAI-compatible LLM API)** to generate a joke based on the weather.

---

## 🚀 Features

- Search any city to get current temperature, wind, humidity, cloud cover, and feels-like temperature.
- Weather icon shown with data.
- A joke generated dynamically based on the weather.
- Clean, minimalistic UI with transparent effects and sharp edges.

---

## 🔑 API Keys Required

To run this project, you must **add your own API keys** for:

1. **WeatherAPI**  
   - Get it here: [https://www.weatherapi.com](https://www.weatherapi.com)
2. **Groq (OpenAI-compatible LLM API)**  
   - Get it here: [https://console.groq.com/keys](https://console.groq.com/keys)

Add your keys in api_keys.py

---

File Structure
WEATHER-APP/
│
├── backend/
│   ├── templates/               # HTML templates for Flask
│   │   └── index.html           # Main frontend interface
│   ├── api_keys.py              # Stores or loads API keys (WeatherAPI + Groq)
│   ├── app.py                   # Flask backend application entry point
│   ├── test_weather.py          # Unit test script for weather functionality
│   └── weather_utils.py         # Weather-related utility functions


