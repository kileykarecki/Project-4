# Project-4

## Wait Less, Play More: Data-Driven Itinerary Planning
### Presentation Date: 1/30/25

### Project Overview: 
Automatically create the best itinerary for your Disney park of choice depending on wait times, popular times, your start time, and party size. 
The goal of this project is to create a Smart Park Planner that helps visitors to Disney parks optimize their schedules based on predicted wait times, visitor flow patterns, and personalized preferences.
This project focuses on Disneyland and Disney California Adventure in Anaheim, CA, USA. 

### Using this Project:
- Use our interactive Leaflet map to input your desired date and time for either Disneyland or Disney California Adventure. View the desired park map with its respective high/low traffic areas, predicted wait times for the rides, and the predicted weather for the day. 
- You can view the final dashboard and leaflet map in the repo above or directly using the following links:
    - Dashboard https://mbee19.github.io/project-4-demo/dashboard.html
    - Leaflet map https://mbee19.github.io/project-4-demo/leaflet.html

### Team Members: 
- Brian Hester
    - Collect and clean historical weather data
    - Heatmap visualizations for peak wait times at each park
- Israel Flores
    - Scrape websites for data, make calls to API to create datasets
    - Build Classification Model to show high and low traffic areas
- Jenny Liu
    - Collect coordinates data for rides at each park
    - Create Leaflet map for final visualization and presentation
    - HTML/CSS Implementation for final Dashboard
- Jimmy Lee
    - Build Classification Model to show high and low traffic areas
    - Develop Gamma.app presentaion
- Kiley Karecki
    - Source theme park data for predictive models
    - Build Regression Model to predict wait times at given rides
- Morgan Bee
    - Build Regression Model for predicting weather at various parks
    - HTML/CSS Implementation for final Dashboard

### Project Timeline: 
- 1/22/25: Datasets to be used finalized and downloaded appropriately
- 1/23/25: API Calls completed, data cleaned, begin building models and visualizations
- 1/27/25: Aim to have most coding and visualizations completed by the end of class
- 1/29/25: Finalize presentation and submit
- 1/30/25: Presentation during class

### Data Sources
- Weather: https://dev.meteostat.net/ 
- Ride Wait Time Data: 
    - Disneyland:  https://www.thrill-data.com/waittimes/disneyland
    - Disney California Adventure:  https://www.thrill-data.com/waittimes/california-adventure
- Ride Coordinates Data: https://api.themeparks.wiki/v1/entity/bfc89fd6-314d-44b4-b89e-df1a89cf991e/children 

### Limitations of our Data
In this project, we had high hopes for the amount of data we would be able to find regarding the various Disney Parks around the world and their respective ride wait times. Unfortunately, most of this data available on the internet is fragmented, outdated, or both. We attempted to scrape information from the Queue Times
website with no luck, and also made several calls to the Queue Times API. This API is exclusively a real-time information source, so we were unable to retrieve historical wait time data through this avenue. Finally, we landed on our final dataset from thrill-data.com (full url listed in our sources section) that pulled data from January 2024 - December 2024 for both Disneyland and Disney California Adventure. That being said, the various models in our project that predict wait times and high or low traffic areas in the park were trained on data from 2024 only. 

### Models
#### Predicting Wait Times (Decision Tree Regressor Model)
- Problem: Help park visitors predict ride wait times based on factors such as the time of day, day of the week, weather, season, or special events.
- Approach: Use historical wait time data for various attractions. Train a regression model to predict wait times for specific rides.
- Output: A recommended route based on predicted low wait time slots.

#### Peak Time Prediction (Classification Model)
- Problem: Predict whether a ride or area of the park will experience high traffic at a given time.
- Approach: Use historical data to train a classification model to label times as “high traffic” or “low traffic.”
- Output: A heat map of peak and off-peak times for park areas.

#### Weather Prediction (Decision Tree Regressor Model)
- Problem: Predict weather (average temperature) at any park for a specific day using user input. 
- Approach: Use 5 years of historical weather data to train a Decision Tree Regressor model to predict an average temperature for a future date. 
- Output: A simple temperature prediction for the day entered.

#### Model Implementation
- The three models can be used simultaneously so that you can first narrow down the high or low-traffic areas of the park, pick specific rides based on wait time when you arrive at the line, and know the expected average temperature during your day. Overall, our models will help parkgoers to wait in lines for the least amount of time, maximizing their ride minutes and extending the value of their theme park tickets.

### Code sources and other helpful information used for this project: 
Throughout this project, we referred to the class lecture notes and slides, activities, and challenges to help develop our code. Please see specific articles and other sources here for each individual model. 

AI programs like OpenAI's Chat GPT and Xpert Learning Assistant were used throughout this project. Specific citations are provided throughout the project where necessary. 

#### Wait Time Prediction Model: 
- Youtube videos by compsci112358, Greg Kamradt, and Data Professor
- ChatGPT (Code cited in Notebooks where used)
- Xpert Learning Assistant (Code cited in Notebooks where used)

#### High/Low Traffic Prediction Model: 

#### Weather Prediction Model
- https://www.geeksforgeeks.org/random-forest-regression-in-python/
- https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.OneHotEncoder.html
- https://albertum.medium.com/preprocessing-onehotencoder-vs-pandas-get-dummies-3de1f3d77dcc
- https://www.geeksforgeeks.org/python-implementation-of-polynomial-regression/
- https://medium.com/@shuv.sdr/polynomial-regression-in-python-58198fb0973f
- https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.PolynomialFeatures.html
- Xpert Learning Assistant (Code cited in Notebooks where used)

#### Dashboard
- photo from: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F806144402042297415%2F&psig=AOvVaw2jYAxbUHU_wUkjiXaWeJV2&ust=1738279904227000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMDK9rOLnIsDFQAAAAAdAAAAABAE 
- Edited with Canva (Pro version)
- Xpert Learning Assistant and OpenAI's Chat GPT used throughout. Cited specifically within code. 

#### Presentation/Slide Deck

- Presentation theme adapted from SlideNest using a commercial account and imported into Gamma.app for use
- Source: https://slidenest.com/template/carnival-games-theme-presentation

####
