"""Computing aggregations
You'll now compute summary statistics by aggregating NumPy arrays across various dimensions (in this case, giving trends in electricity usage).

The load_recent_3d NumPy array from the last exercise is provided for you. It contains the electricity load (in kWh) sampled every 15 minutes from the start of 2013 to the end of 2015. The possible index values of the three-dimensional array correspond to year (from 0 to 2), day (from 0 to 364), and 15-minute interval (from 0 to 95); remember, NumPy arrays are indexed from zero. Thus, load_recent_3d[0,1,2] is the electricity load consumed on January 2nd, 2013 from 00:30:00 AM to 00:45:00 AM"""
# Print mean value of load_recent_3d
print(load_recent_3d.mean())

# Print maximum of load_recent_3d across 2nd & 3rd dimensions
print(load_recent_3d.max(axis=(1,2)))

# Compute sum along last dimension of load_recent_3d: daily_consumption
daily_consumption = load_recent_3d.sum(axis=-1)

# Print mean of 62nd row of daily_consumption
print(daily_consumption[:,61].mean())