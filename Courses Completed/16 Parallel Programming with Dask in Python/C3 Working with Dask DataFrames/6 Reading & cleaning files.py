"""Reading & cleaning files
Here you'll be working with a subset of the NYC Taxi Trip data. The first step is to use the Dask dd.read_csv() function to read multiple files at once. Dask will automatically concatenate the contents of the files into a single DataFrame. Notice that you'll use the option assume_missing=True in the call to dd.read_csv() to suppress warning messages.

Your job is to use a glob pattern containing the * character to read all of the CSV files from the taxi/ subdirectory into a single Dask DataFrame. You'll then construct a new column called 'tip_fraction' using the 'tip_amount' and 'total_amount' columns. The 'total_amount' is the sum of the fare, other fees, and the tip_amount.

Instructions
Read all .csv files from the taxi/ directory (with a wildcard pattern *).
Create a column 'tip_fraction', which is the result of the 'tip_amount' divided by the difference of the 'total_amount' and 'tip_amount' columns.
Convert the 'tpep_dropoff_datetime' column to datetime using dd.to_datetime().
Create a column 'hour' using the .dt.hour attribute of the 'tpep_dropoff_datetime' column.
"""


# Read all .csv files: df
df = dd.read_csv('taxi/*.csv', assume_missing=True)

# Make column 'tip_fraction'
df['tip_fraction'] = df['tip_amount'] / (df['total_amount'] - df['tip_amount'])

# Convert 'tpep_dropoff_datetime' column to datetime objects
df['tpep_dropoff_datetime'] = dd.to_datetime(df['tpep_dropoff_datetime'])

# Construct column 'hour'
df['hour'] = df['tpep_dropoff_datetime'].dt.hour