"""
The long and the short of why time is hard
Out of 291 trips taken by W20529, how long was the longest? How short was the shortest? Does anything look fishy?

As before, data has been loaded as onebike_durations.

Instructions
100 XP
Calculate shortest_trip from onebike_durations.
Calculate longest_trip from onebike_durations.
Print the results, turning shortest_trip and longest_trip into strings so they can print.

"""

# Calculate shortest and longest trips
shortest_trip = min(onebike_durations)
longest_trip = max(onebike_durations)

# Print out the results
print("The shortest trip was " + str(shortest_trip)+ " seconds")
print("The longest trip was " + str(longest_trip) + " seconds")