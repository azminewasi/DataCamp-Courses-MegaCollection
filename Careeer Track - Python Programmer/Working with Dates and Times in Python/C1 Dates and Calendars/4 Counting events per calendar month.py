"""Counting events per calendar month
Hurricanes can make landfall in Florida throughout the year. As we've already discussed, some months are more hurricane-prone than others.

Using florida_hurricane_dates, let's see how hurricanes in Florida were distributed across months throughout the year.

We've created a dictionary called hurricanes_each_month to hold your counts and set the initial counts to zero. You will loop over the list of hurricanes, incrementing the correct month in hurricanes_each_month as you go, and then print the result.

Instructions

Within the for loop:
Assign month to be the month of that hurricane.
Increment hurricanes_each_month for the relevant month by 1.
"""

# A dictionary to count hurricanes per calendar month
hurricanes_each_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6:0,
		  				 7: 0, 8:0, 9:0, 10:0, 11:0, 12:0}

# Loop over all hurricanes
for hurricane in florida_hurricane_dates:
  # Pull out the month
  month = hurricane.month
  # Increment the count in your dictionary by one
  hurricanes_each_month[month] =hurricanes_each_month[month]+1
  
print(hurricanes_each_month)