import requests
import csv

API_KEY = "e734076ab9778d116572a7cda39262c1"
latitude = 33.8121
longitude = -117.919

url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "lat": latitude,
    "lon": longitude,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    # Extract relevant fields
    weather_data = {
        "location": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"],
        "date_time": data["dt"]
    }
    # Save to a CSV file
    with open("weather_data.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=weather_data.keys())
        writer.writeheader()
        writer.writerow(weather_data)
    print("Weather data saved to weather_data.csv!")
else:
    print(f"Error: {response.status_code}")
