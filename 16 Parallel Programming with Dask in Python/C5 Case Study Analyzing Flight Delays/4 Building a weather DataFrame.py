"""Building a weather DataFrame
Your job now is to construct a Dask DataFrame using the function from the previous exercise. To do this, you will iterate over the list filenames provided and build up a list of delayed DataFrames. You'll then concatenate those delayed DataFrames into a Dask DataFrame with dd.from_delayed() as you did with the flight information. Finally, you'll print the row with largest 'Max TemperatureF' value.

The list filenames contains the names of the CSV files of weather data labelled by airport code for Atlanta, Denver, Dallas-Fort Worth, Orlando, and Chicago. The read_weather function from the previous exercise is also provided for you and dask.dataframe is imported as dd. Additionally, an empty list called weather_dfs has been created for you.

Instructions
Loop over filenames with filename as the iterator variable.
Call read_weather() on filename and append the output to weather_dfs.
After the loop, invoke dd.from_delayed() on weather_dfs.
Compute and print the output of weather.nlargest(1, 'Max TemperatureF').
"""

# Loop over filenames with filename
for filename in filenames:
    # Invoke read_weather on filename; append result to weather_dfs
    weather_dfs.append(read_weather(filename))

# Call dd.from_delayed() with weather_dfs: weather
weather = dd.from_delayed(weather_dfs)

# Print result of weather.nlargest(1, 'Max TemperatureF')
print(weather.nlargest(1, 'Max TemperatureF').compute())