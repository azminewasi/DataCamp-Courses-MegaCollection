"""Filtering & grouping data
You have the Dask dataframe df prepared using multiple CSV files from the last exercise. It contains a subset of the 2015 yellow taxi ride data from New York City with some additional columns from preprocessing. Remember, none of the files have actually been loaded, nor has any computation been done to construct the new columns.

Your task now is to build a pipeline of computations to compute the hourly average tip fraction for each hour of the day across the entire year of data. You'll have to filter for payments of type 1 (credit card transactions) from the 'payment_type' column, group transactions using the 'hour' column, and finally aggregate the mean from the 'tip_fraction' column.

Instructions
Filter out rows where payment_type is 1 and call the resulting dataframe credit.
Group credit using the 'hour' column and call the result 'hourly'.
Select the 'tip_fraction' column and aggregate the mean.
Display the data type of result.
"""

# Filter rows where payment_type == 1: credit
credit = df[df.payment_type == 1]

# Group by 'hour' column: hourly
hourly = credit.groupby("hour")

# Aggregate mean 'tip_fraction' and print its data type
result = hourly['tip_fraction'].mean()
print(type(result))