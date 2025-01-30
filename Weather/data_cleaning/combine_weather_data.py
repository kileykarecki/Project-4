import pandas as pd

# List of CSV files to combine
files = [
    'disneyland_anaheim_weather.csv',
    'epcot_weather.csv',
    'paris_weather.csv',
    'hong_kong_weather.csv'
]

# Read each file and add a column indicating the location
dataframes = []
locations = ['Anaheim', 'Epcot', 'Paris', 'Hong Kong']
for file, location in zip(files, locations):
    df = pd.read_csv(file)
    df['Location'] = location  # Add a location column
    dataframes.append(df)

# Combine all dataframes
combined_data = pd.concat(dataframes)

# Save combined data to a new CSV file
combined_data.to_csv('combined_disney_weather.csv', index=False)
print("Combined data saved to 'combined_disney_weather.csv'")