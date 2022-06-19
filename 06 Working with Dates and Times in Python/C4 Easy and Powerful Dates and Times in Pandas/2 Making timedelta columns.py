"""Making timedelta columns
Earlier in this course, you wrote a loop to subtract datetime objects and determine how long our sample bike had been out of the docks. Now you'll do the same thing with Pandas.

rides has already been loaded for you.

Instructions
100 XP
Subtract the Start date column from the End date column to get a Series of timedeltas; assign the result to ride_durations.
Convert ride_durations into seconds and assign the result to the 'Duration' column of rides."""

# Subtract the start date from the end date
ride_durations =rides['End date'] - rides['Start date']

# Convert the results to seconds
rides['Duration'] = ride_durations.dt.total_seconds()

print(rides['Duration'].head())