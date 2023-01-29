"""Turning pairs of datetimes into durations
When working with timestamps, we often want to know how much time has elapsed between events. Thankfully, we can use datetime arithmetic to ask Python to do the heavy lifting for us so we don't need to worry about day, month, or year boundaries. Let's calculate the number of seconds that the bike was out of the dock for each trip.

Continuing our work from a previous coding exercise, the bike trip data has been loaded as the list onebike_datetimes. Each element of the list consists of two datetime objects, corresponding to the start and end of a trip, respectively.

Instructions
Within the loop:
Use arithmetic on the start and end elements to find the length of the trip
Save the results to trip_duration.
Calculate trip_length_seconds from trip_duration."""

# Initialize a list for all the trip durations
onebike_durations = []

for trip in onebike_datetimes:
  # Create a timedelta object corresponding to the length of the trip
  trip_duration = trip['end'] - trip['start']
  
  # Get the total elapsed seconds in trip_duration
  trip_length_seconds = trip_duration.total_seconds()
  
  # Append the results to our list
  onebike_durations.append(trip_length_seconds)