"""Putting a list of dates in order
Much like numbers and strings, date objects in Python can be put in order. Earlier dates come before later ones, and so we can sort a list of date objects from earliest to latest.

What if our Florida hurricane dates had been scrambled? We've gone ahead and shuffled them so they're in random order and saved the results as dates_scrambled. Your job is to put them back in chronological order, and then print the first and last dates from this sorted list."""

# Print the first and last scrambled dates
print(dates_scrambled[0])
print(dates_scrambled[-1])

# Put the dates in order
dates_ordered = sorted(dates_scrambled)

# Print the first and last ordered dates
print(dates_ordered[0])
print(dates_ordered[-1])