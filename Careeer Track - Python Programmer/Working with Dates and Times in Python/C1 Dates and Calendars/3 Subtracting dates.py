"""Subtracting dates
Python date objects let us treat calendar dates as something similar to numbers: we can compare them, sort them, add, and even subtract them. This lets us do math with dates in a way that would be a pain to do by hand.

The 2007 Florida hurricane season was one of the busiest on record, with 8 hurricanes in one year. The first one hit on May 9th, 2007, and the last one hit on December 13th, 2007. How many days elapsed between the first and last hurricane in 2007?

Instructions
Import date from datetime.
Create a date object for May 9th, 2007, and assign it to the start variable.
Create a date object for December 13th, 2007, and assign it to the end variable.
Subtract start from end, to print the number of days in the resulting timedelta object."""

# Import date
from datetime import date

# Create a date object for May 9th, 2007
start = date(2007, 5, 9)

# Create a date object for December 13th, 2007
end = date(2007, 12,13)

# Subtract the two dates and print the number of days
print((end - start).days)