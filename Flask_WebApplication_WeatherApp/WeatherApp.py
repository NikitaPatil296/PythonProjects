from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Your OpenWeatherMap API Key
API_KEY = os.environ.get('API_KEY')

# Function to get the user's current location using IP geolocation
def get_current_location():
    try:
        response = requests.get("https://ipapi.co/json/")
        response.raise_for_status()
        location_data = response.json()
        return location_data.get("city", ""), location_data.get("country", "")
    except requests.exceptions.RequestException:
        return None, None

# Function to fetch weather data from OpenWeatherMap
def get_weather_data(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Function to format weather data
def format_weather(data):
    if "error" in data:
        return {"error": data["error"]}
    if data.get("cod") != 200:
        return {"error": data.get("message", "Unable to fetch weather data.")}
    
    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"].capitalize(),
        "wind_speed": data["wind"]["speed"],
        "pressure": data["main"]["pressure"],
        "visibility": data.get("visibility", 0) / 1000  # Convert to km if available
    }

# Home route
@app.route('/')
def home():
    return render_template("index.html")

# API route for current location weather
@app.route('/api/current_location', methods=['GET'])
def current_location_weather():
    city, _ = get_current_location()
    if not city:
        return jsonify({"error": "Unable to detect current location."}), 400
    weather_data = get_weather_data(city)
    formatted_weather = format_weather(weather_data)
    return jsonify(formatted_weather)

# API route for fetching weather by city
@app.route('/api/weather', methods=['POST'])
def weather_by_city():
    data = request.json
    city = data.get("city")
    if not city:
        return jsonify({"error": "City name is required."}), 400
    weather_data = get_weather_data(city)
    formatted_weather = format_weather(weather_data)
    return jsonify(formatted_weather)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # 0.0.0.0 allows external access
