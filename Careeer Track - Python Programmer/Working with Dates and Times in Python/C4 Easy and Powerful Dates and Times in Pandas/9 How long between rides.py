"""How long between rides?
For your final exercise, let's take advantage of Pandas indexing to do something interesting. How much time elapsed between rides?

Instructions
100 XP
Calculate the difference in the Start date of the current row and the End date of the previous row and assign it to rides['Time since'].
Convert rides['Time since'] to seconds to make it easier to work with.
Resample rides to be in monthly buckets according to the Start date.
Divide the average by (60*60) to get the number of hours on average that W20529 waited in the dock before being picked up again.
"""

# Shift the index of the end date up one; now subract it from the start date
rides['Time since'] = rides['Start date'] - (rides['End date'].shift(1))

# Move from a timedelta to a number of seconds, which is easier to work with
rides['Time since'] = rides['Time since'].dt.total_seconds()

# Resample to the month
monthly = rides.resample('M', on = 'Start date')

# Print the average hours between rides each month
print(monthly['Time since'].mean()/(60*60))