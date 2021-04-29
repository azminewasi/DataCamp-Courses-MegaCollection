"""Finding ambiguous datetimes
At the end of lesson 2, we saw something anomalous in our bike trip duration data. Let's see if we can identify what the problem might be.

The data is loaded as onebike_datetimes, and tz has already been imported from dateutil.

Instructions
100 XP
Loop over the trips in onebike_datetimes:
Print any rides whose start is ambiguous.
Print any rides whose end is ambiguous."""

# Loop over trips
for trip in onebike_datetimes:
  # Rides with ambiguous start
  if tz.datetime_ambiguous(trip['start']):
    print("Ambiguous start at " + str(trip['start']))
  # Rides with ambiguous end
  if tz.datetime_ambiguous(trip['end']):
    print("Ambiguous end at " + str(trip['end']))