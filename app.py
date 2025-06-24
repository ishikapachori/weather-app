from flask import Flask,request, jsonify,render_template
from flask_cors import CORS
from weather_utils import get_weather,get_weather_joke

app=Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_weather_joke", methods=["GET"])
def get_weather_joke_api():
    city = request.args.get("city")
    print(f"Received request for city: {city}")

    weather_info = get_weather(city)
    if not weather_info:
        print("Weather info not found.")
        return jsonify({"error": "Failed to fetch weather data"}), 500

    joke = get_weather_joke(weather_info)
    return jsonify({"weather": weather_info, "joke": joke})

if __name__=='__main__':
    app.run(debug=True)