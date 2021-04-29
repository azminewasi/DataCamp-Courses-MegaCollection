"""Setting timezones
Now that you have the hang of setting timezones one at a time, let's look at setting them for the first ten trips that W20529 took.

timezone and timedelta have already been imported. Make the change using .replace()

Instructions
100 XP
Create edt, a timezone object whose UTC offset is -4 hours.
Within the for loop:
Set the tzinfo for trip['start'].
Set the tzinfo for trip['end'].
"""

# Create a timezone object corresponding to UTC-4
edt = timezone(timedelta(hours=-4))

# Loop over trips, updating the start and end datetimes to be in UTC-4
for trip in onebike_datetimes[:10]:
  # Update trip['start'] and trip['end']
  trip['start'] = trip['start'].replace(tzinfo=edt)
  trip['end'] = trip['end'].replace(tzinfo=edt)