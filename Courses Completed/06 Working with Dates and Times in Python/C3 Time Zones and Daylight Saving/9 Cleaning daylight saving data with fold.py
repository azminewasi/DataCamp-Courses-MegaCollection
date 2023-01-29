"""
Cleaning daylight saving data with fold
As we've just discovered, there is a ride in our data set which is being messed up by a Daylight Savings shift. Let's clean up the data set so we actually have a correct minimum ride length. We can use the fact that we know the end of the ride happened after the beginning to fix up the duration messed up by the shift out of Daylight Savings.

Since Python does not handle tz.enfold() when doing arithmetic, we must put our datetime objects into UTC, where ambiguities have been resolved.

onebike_datetimes is already loaded and in the right timezone. tz and timezone have been imported. Use tz.UTC for the timezone.

Instructions

Complete the if statement to be true only when a ride's start comes after its end.
When start is after end, call tz.enfold() on the end so you know it refers to the one after the daylight savings time change.
After the if statement, convert the start and end to UTC so you can make a proper comparison.

"""

trip_durations = []
for trip in onebike_datetimes:
  # When the start is later than the end, set the fold to be 1
  if trip['start'] > trip['end']:
    trip['end'] = tz.enfold(trip['end'])
  # Convert to UTC
  start = trip['start'].astimezone(tz.UTC)
  end = trip['end'].astimezone(tz.UTC)

  # Subtract the difference
  trip_length_seconds = (end-start).total_seconds()
  trip_durations.append(trip_length_seconds)

# Take the shortest trip duration
print("Shortest trip: " + str(min(trip_durations)))