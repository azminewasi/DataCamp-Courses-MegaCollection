"""
Recreating ISO format with strftime()
In the last chapter, you used strftime() to create strings from date objects. Now that you know about datetime objects, let's practice doing something similar.

Re-create the .isoformat() method, using .strftime(), and print the first trip start in our data set.

Reference	
%Y	4 digit year (0000-9999)
%m	2 digit month (1-12)
%d	2 digit day (1-31)
%H	2 digit hour (0-23)
%M	2 digit minute (0-59)
%S	2 digit second (0-59)
Instructions
Complete fmt to match the format of ISO 8601.
Print first_start with both .isoformat() and .strftime(); they should match.


"""

# Import datetime
from datetime import datetime

# Pull out the start of the first trip
first_start = onebike_datetimes[0]['start']

# Format to feed to strftime()
fmt = "%Y-%m-%dT%H:%M:%S"

# Print out date with .isoformat(), then with .strftime() to compare
print(first_start.isoformat())
print(first_start.strftime(fmt))