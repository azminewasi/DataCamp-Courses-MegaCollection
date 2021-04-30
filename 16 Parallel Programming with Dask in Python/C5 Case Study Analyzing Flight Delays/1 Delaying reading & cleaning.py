"""Delaying reading & cleaning
To work with this subset of the monthly flight information data efficiently, you'll need to do a bit of cleaning. Specifically, you'll need to replace zeros in the 'WEATHER_DELAY' column with nan. This substitution will make counting delays much easier later. This operation requires you to build a delayed pipeline of pandas DataFrame manipulations. You will then convert the output to a Dask DataFrame in which each file will be one chunk.

Your first job is to write a function to read a single CSV file into a DataFrame. The DataFrame returned will use pandas TimeStamps in the 'FL_DATE' column, and will have 0s replaced with np.nans in the 'WEATHER_DELAY' column. You can use the flightdelays-2016-1.csv file to verify that the function works as intended.

Instructions
Define the @delayed-function read_flights that takes a filename as input.
Within the function, read filename into a DataFrame with parse_dates=['FL_DATE'].
Using .replace(), replace all the 0s in df['WEATHER_DELAY'] with np.nan"""

# Define @delayed-function read_flights
@delayed
def read_flights(filename):

    # Read in the DataFrame: df
    df = pd.read_csv(filename, parse_dates=['FL_DATE'])

    # Replace 0s in df['WEATHER_DELAY'] with np.nan
    df['WEATHER_DELAY'] = df['WEATHER_DELAY'].replace(0, np.nan)

    # Return df
    return df