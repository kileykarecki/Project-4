from meteostat import Point, Daily
from datetime import datetime
import pandas as pd

# Define the location for Disneyland Hong Kong (China)
location = Point(22.3129, 114.0411)  # Latitude, Longitude

# Define the date range (5 years)
start_date = datetime(2018, 1, 1)  # Start date
end_date = datetime(2023, 12, 31)  # End date

# Fetch daily weather data
data = Daily(location, start_date, end_date)
data = data.fetch()

# Save data to a CSV file
data.to_csv('hong_kong_weather.csv')
print("Weather data saved to 'hong_kong_weather.csv'")

# Preview the data
print(data.head())