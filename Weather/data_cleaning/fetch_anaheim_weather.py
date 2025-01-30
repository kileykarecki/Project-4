from meteostat import Point, Daily
from datetime import datetime
import pandas as pd

# Define the location for Disneyland Anaheim
location = Point(33.8121, -117.919)  # Latitude, Longitude

# Define the date range (5 years)
start_date = datetime(2018, 1, 1)  # Start date
end_date = datetime(2023, 12, 31)  # End date

# Fetch daily weather data
data = Daily(location, start_date, end_date)
data = data.fetch()

# Save data to a CSV file
data.to_csv('disneyland_anaheim_weather.csv')
print("Weather data saved to 'disneyland_anaheim_weather.csv'")

# Preview the data
print(data.head())
