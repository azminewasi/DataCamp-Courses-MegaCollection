"""Printing dates in a friendly format
Because people may want to see dates in many different formats, Python comes with very flexible functions for turning date objects into strings.

Let's see what event was recorded first in the Florida hurricane data set. In this exercise, you will format the earliest date in the florida_hurriance_dates list in two ways so you can decide which one you want to use: either the ISO standard or the typical US style.

Instructions
Assign the earliest date in florida_hurricane_dates to first_date.
Print first_date in the ISO standard. For example, December 1st, 2000 would be "2000-12-01".
Print first_date in the US style, using .strftime(). For example, December 1st, 2000 would be "12/1/2000" .
"""

# Assign the earliest date to first_date
first_date = min(florida_hurricane_dates)

# Convert to ISO and US formats
iso = "Our earliest hurricane date: " + first_date.isoformat()
us = "Our earliest hurricane date: " + first_date.strftime('%m/%d/%Y')

print("ISO: " + iso)
print("US: " + us)