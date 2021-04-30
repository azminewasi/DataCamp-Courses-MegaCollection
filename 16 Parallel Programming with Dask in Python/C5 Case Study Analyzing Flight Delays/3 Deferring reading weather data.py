"""Deferring reading weather data
For this exercise, daily weather data is provided from 2016 for 5 US cities: Atlanta, Denver, Dallas-Fort Worth, Orlando, and Chicago. The weather data comes from Weather Underground and is found in separate CSV files labelled by airport code (e.g., ATL.csv). The list filenames contains the names of these 5 files. The ultimate goal is to correlate the flight delays with weather events from each day of 2016.

As with the flight-delays data, you'll need to clean the weather data as it is read in. Your job is to define a function that loads a DataFrame from a file, cleans the DataFrame's 'PrecipitationIn' column, and appends an 'Airport' column with the appropriate airport code for each record.

Instructions
Define an @delayed-function read_weather that takes filename as input.
Read filename using read_csv() with parse_dates=['Date'] into a DataFrame called df.
Clean the 'PrecipitationIn' column using pd.to_numeric(df['PrecipitationIn'], errors='coerce').
Create a column with the airport code called 'Airport' using filename.split('.')[0].
"""

# Define @delayed-function read_weather with input filename
@delayed
def read_weather(filename):
    # Read in filename: df
    df = pd.read_csv(filename, parse_dates=['Date'])

    # Clean 'PrecipitationIn'
    df['PrecipitationIn'] = pd.to_numeric(df['PrecipitationIn'], errors='coerce')

    # Create the 'Airport' column
    df['Airport'] = filename.split('.')[0]

    # Return df
    return df