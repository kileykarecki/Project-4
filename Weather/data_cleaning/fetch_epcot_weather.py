from meteostat import Point, Daily
from datetime import datetime
import pandas as pd

# Define the location for Disneyworld Epcot
location = Point(28.3772, -81.5707)  # Latitude, Longitude

# Define the date range (5 years)
start_date = datetime(2018, 1, 1)  # Start date
end_date = datetime(2023, 12, 31)  # End date

# Fetch daily weather data
data = Daily(location, start_date, end_date)
data = data.fetch()

# Save data to a CSV file
data.to_csv('disneyworld_epcot_weather.csv')
print("Weather data saved to 'disneyworld_epcot_weather.csv'")

# Preview the data
print(data.head())
