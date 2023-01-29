"""
Turning strings into datetimes
When you download data from the Internet, dates and times usually come to you as strings. Often the first step is to turn those strings into datetime objects.

In this exercise, you will practice this transformation.

Reference	
%Y	4 digit year (0000-9999)
%m	2 digit month (1-12)
%d	2 digit day (1-31)
%H	2 digit hour (0-23)
%M	2 digit minute (0-59)
%S	2 digit second (0-59)"""

"""
Determine the format needed to convert s to datetime and assign it to fmt.
Convert the string s to datetime using fmt.
"""

# Import the datetime class
from datetime import datetime

# Starting string, in YYYY-MM-DD HH:MM:SS format
s = '2017-02-03 00:00:01'

# Write a format string to parse s
fmt = '%Y-%m-%d %H:%M:%S'

# Create a datetime object d
d = datetime.strptime(s,fmt)

# Print d
print(d)


"""
Determine the format needed to convert s to datetime and assign it to fmt.
Convert the string s to datetime using fmt."""

# Import the datetime class
from datetime import datetime

# Starting string, in YYYY-MM-DD format
s = '2030-10-15'

# Write a format string to parse s
fmt = '%Y-%m-%d'

# Create a datetime object d
d = datetime.strptime(s,fmt)

# Print d
print(d)

"""Determine the format needed to convert s to datetime and assign it to fmt.
Convert the string s to datetime using fmt."""
# Import the datetime class
from datetime import datetime

# Starting string, in MM/DD/YYYY HH:MM:SS format
s = '12/15/1986 08:00:00'

# Write a format string to parse s
fmt = '%m/%d/%Y %H:%M:%S'

# Create a datetime object d
d = datetime.strptime(s,fmt)

# Print d
print(d)