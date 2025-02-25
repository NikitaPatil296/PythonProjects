import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

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
def get_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Function to display weather in a formatted and professional manner
def format_weather(data):
    if "error" in data:
        return f"Error: {data['error']}"
    if data.get("cod") != 200:
        return f"Error: {data.get('message', 'Unable to fetch weather data.')}"
    
    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"].capitalize()
    wind_speed = data["wind"]["speed"]
    pressure = data["main"]["pressure"]
    visibility = data.get("visibility", 0) / 1000  # Convert to km if available

    return (
        f"{city}, {country}\n\n"
        f"Temperature: {temp}°C\n"
        f"Feels Like: {feels_like}°C\n"
        f"Humidity: {humidity}%\n"
        f"Condition: {weather}\n"
        f"Wind Speed: {wind_speed} km/h\n"
        f"Visibility: {visibility:.1f} km\n"
        f"Pressure: {pressure} hPa"
    )

# Function to update the weather for the current location
def fetch_current_location_weather():
    city, country = get_current_location()
    if not city:
        messagebox.showerror("Error", "Unable to detect current location.")
        return
    weather_data = get_weather_data(city, api_key)
    weather_details.set(format_weather(weather_data))

# Function to fetch weather based on user input
def fetch_weather_by_city():
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name.")
        return
    weather_data = get_weather_data(city, api_key)
    weather_details.set(format_weather(weather_data))




# Main Application
root = tk.Tk()
root.title("Weather App")
root.geometry("400x450")
root.resizable(False, False)

# Your OpenWeatherMap API Key
api_key = "" 

# Weather Details Variable
weather_details = tk.StringVar()
weather_details.set("Fetching weather for your location...")

# Current Location Button
current_location_button = tk.Button(
    root, text="Get Current Location Weather", command=fetch_current_location_weather,
    font=("Helvetica", 12), bg="#4CAF50", fg="white"
)
current_location_button.pack(pady=10)

# Weather Display Area
weather_frame = tk.Frame(root, bg="#F9F9F9", relief="groove", bd=2)
weather_frame.pack(pady=20, padx=20, fill="both", expand=True)

weather_label = tk.Label(
    weather_frame, textvariable=weather_details, font=("Helvetica", 12), justify="left",
    wraplength=400, anchor="nw", padx=10, pady=10
)
weather_label.pack(fill="both", expand=True)

# City Search Input
city_label = tk.Label(root, text="Enter City Name:", font=("Helvetica", 12))
city_label.pack(pady=5)

city_entry = tk.Entry(root, font=("Helvetica", 12))
city_entry.pack(pady=5)

# Fetch Button
fetch_button = tk.Button(
    root, text="Get Weather", command=fetch_weather_by_city,
    font=("Helvetica", 12), bg="#4CAF50", fg="white"
)
fetch_button.pack(pady=10)


# Fetch weather for current location on startup
fetch_current_location_weather()  

# Run the application
root.mainloop()
