"""Finding sources of weather delays
The final step in this case study is to use the persisted_weather_delays Dask DataFrame to determine the percentage of delayed flights per weather event.

Your job is to compute the number of delayed flights by weather events and divide by the total number of flights. You'll then use .nlargest(5) to retrieve the five highest contributions to the number of delayed flights. Finally, you'll compute the average length of the delay for the 5 leading contributions.

Instructions
Count the by_event['WEATHER_DELAY'] column and divide by the total number of delayed flights from persisted_weather_delays, multiply by 100 and assign the result to pct_delayed.
Compute & print the five largest values of pct_delayed with .nlargest(5).
Calculate the mean of the by_event['WEATHER_DELAY'] column and return the 5 largest entries with .nlargest(5).
Compute & print avg_delay_time."""

# Group persisted_weather_delays by 'Events': by_event
by_event = persisted_weather_delays.groupby('Events')

# Count 'by_event['WEATHER_DELAY'] column & divide by total number of delayed flights
pct_delayed = by_event['WEATHER_DELAY'].count() / persisted_weather_delays['WEATHER_DELAY'].count() * 100

# Compute & print five largest values of pct_delayed
print(pct_delayed.nlargest(5).compute())

# Calculate mean of by_event['WEATHER_DELAY'] column & return the 5 largest entries: avg_delay_time
avg_delay_time = by_event['WEATHER_DELAY'].mean().nlargest(5)

# Compute & print avg_delay_time
print(avg_delay_time.compute())