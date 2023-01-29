"""
Putting the bike trips into the right time zone
Instead of setting the timezones for W20529 by hand, let's assign them to their IANA timezone: 'America/New_York'. Since we know their political jurisdiction, we don't need to look up their UTC offset. Python will do that for us.

Instructions
100 XP
Import tz from dateutil.
Assign et to be the timezone 'America/New_York'.
Within the for loop, set start and end to have et as their timezone (use .replace()).
"""

# Import tz
from dateutil import tz
# Create a timezone object for Eastern Time
et = tz.gettz('America/New_York')

# Loop over trips, updating the datetimes to be in Eastern Time
for trip in onebike_datetimes[:10]:
  # Update trip['start'] and trip['end']
  trip['start'] = trip['start'].replace(tzinfo=et)
  trip['end'] = trip['end'].replace(tzinfo=et)

"""  Make the Start date column timezone aware by localizing it to 'America/New_York' while ignoring any ambiguous datetimes."""

# Localize the Start date column to America/New_York
rides['Start date'] = rides['Start date'].astimezone(tz.gettz('America/New_York'))

# Print first value
print(rides['Start date'].iloc[0])