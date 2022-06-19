"""Combining groupby() and resample()
A very powerful method in Pandas is .groupby(). Whereas .resample() groups rows by some time or date information, .groupby() groups rows based on the values in one or more columns. For example, rides.groupby('Member type').size() would tell us how many rides there were by member type in our entire DataFrame.

.resample() can be called after .groupby(). For example, how long was the median ride by month, and by Membership type?

Instructions
100 XP
Complete the .groupby() call to group by 'Member type', and the .resample() call to resample according to 'Start date', by month.
Print the median Duration for each group."""

# Group rides by member type, and resample to the month
grouped = rides.groupby('Member type')\
  .resample('M', on="Start date")

# Print the median duration for each group
print(grouped['Duration'].median())