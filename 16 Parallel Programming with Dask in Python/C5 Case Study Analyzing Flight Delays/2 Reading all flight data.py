"""Reading all flight data
A list called filenames is provided for you at the start of this exercise; it contains the strings "flightdelays-2016-1.csv" through "flightdelays-2016-12.csv". In addition, the delayed function read_flights() defined in the last exercise is provided for you. Also, Numpy & Pandas have been imported for you.

Your task now is to iterate over the list filenames and to use the function read_flights to build a list of delayed objects. Finally, you'll concatenate them into a Dask DataFrame with dd.from_delayed() and print out the mean of the WEATHER_DELAY column.

Note: This exercise may take several seconds to execute.

Instructions
Loop over the list filenames with iterator variable filename.
Invoke read_flights on filename and append the output to dataframes.
After the loop, apply dd.from_delayed() to the list dataframes. Assign the result to flight_delays.
Print the average value of the 'WEATHER_DELAY' column of flight_delays."""

# Loop over filenames with index filename
for filename in filenames:
    # Apply read_flights to filename; append to dataframes
    dataframes.append(read_flights(filename))

# Compute flight delays: flight_delays
flight_delays = dd.from_delayed(dataframes)

# Print average of 'WEATHER_DELAY' column of flight_delays
print(flight_delays['WEATHER_DELAY'].mean().compute())