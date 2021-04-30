"""Persisting merged DataFrame
If your data can fit into memory, either on a workstation or a cluster, persisting the Dask DataFrame with the .persist() method can be useful. In particular, persisting DataFrames can provide significant speed-up because the time-consuming work of reading from disk is performed only once.

The following function, which computes the percentage of flights delayed by weather, has been defined for you:

def percent_delayed(df):
    return (df['WEATHER_DELAY'].count() / len(df)) * 100
Your job is to time the execution of that function using the weather_delays DataFrame. You'll then call .persist() on the DataFrame and compare execution times of the function with the persisted DataFrame.

Note: This exercise will take several seconds to execute.

Instructions
Print the time in milliseconds to compute the result of percent_delayed with weather_delays.
Call weather_delays.persist() and assign the result to persisted_weather_delays.
Print the time in milliseconds to compute the result of percent_delayed with persisted_weather_delays."""

# Print time in milliseconds to compute percent_delayed on weather_delays
t_start = time.time()
print(percent_delayed(weather_delays).compute())
t_end = time.time()
print((t_end-t_start)*1000)

# Call weather_delays.persist(): persisted_weather_delays
persisted_weather_delays =weather_delays.persist()

# Print time in milliseconds to compute percent_delayed on persisted_weather_delays
t_start = time.time()
print(percent_delayed(persisted_weather_delays).compute())
t_end = time.time()
print((t_end-t_start)*1000)