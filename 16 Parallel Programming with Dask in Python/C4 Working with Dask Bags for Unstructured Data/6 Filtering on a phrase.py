"""Filtering on a phrase
In this exercise you'll make use of the filter function to take the 226 State of the Union addresses and find the addresses where the phrase health care was mentioned. In order to do this you must first standardize the capitalization of all words in each speech.

Your job is to convert all speeches to lower case and write a lambda function that returns true if the substring 'health care' is contained in each speech and filter with it. Finally, you'll count the number of speeches retained by the filter.

The speeches Dask Bag is provided for you.

Instructions
Convert speeches to lower case.
Filter lower with the lambda function lambda s:'health care' in s and assign to health.
Count the number of entries in health as n_health.
Compute and print the value of n_health."""

# Convert speeches to lower case: lower
lower = speeches.str.lower()

# Filter lower for the presence of 'health care': health
health = lower.filter(lambda s:'health care' in s)

# Count the number of entries : n_health
n_health = health.count()

# Compute and print the value of n_health
print(n_health.compute())