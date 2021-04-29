"""How long per weekday?
Pandas has a number of datetime-related attributes within the .dt accessor. Many of them are ones you've encountered before, like .dt.month. Others are convenient and save time compared to standard Python, like .dt.weekday_name.

Instructions
Add a new column to rides called 'Ride start weekday', which is the weekday of the Start date.
Print the median ride duration for each weekday."""

# Add a column for the weekday of the start of the ride
rides['Ride start weekday'] = rides['Start date'].dt.weekday_name

# Print the median trip time per weekday
print(rides.groupby('Ride start weekday')['Duration'].median())