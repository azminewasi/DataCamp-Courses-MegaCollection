Row selection: loc[] vs iloc[]
A big part of working with DataFrames is to locate specific entries in the dataset. You can locate rows in two ways:

By a specific value of a column (feature).
By the index of the rows (index). In this exercise, we will focus on the second way.
If you have previous experience with pandas, you should be familiar with the .loc and .iloc indexers, which stands for 'location' and 'index location' respectively. In most cases, the indices will be the same as the position of each row in the Dataframe (e.g. the row with index 13 will be the 14th entry).

While we can use both functions to perform the same task, we are interested in which is the most efficient in terms of speed.

Instructions 
Store the indices of the first 1000 rows in the row_nums.
Use the .loc[] indexer to select the first 1000 rows of poker_hands, and record the times before and after that operation.
Print the time it took to select the rows.

==================================================================================================================

# Define the range of rows to select: row_nums
row_nums = range(0, 1000)

# Select the rows using .loc[] and row_nums and record the time before and after
loc_start_time = time.time()
rows = poker_hands.loc[row_nums]
loc_end_time = time.time()

# Print the time it took to select the rows using .loc
print("Time using .loc[]: {} sec".format(loc_end_time - loc_start_time))

# Select the rows using .iloc[] and row_nums and record the time before and after
iloc_start_time = time.time()
rows = poker_hands.iloc[:1000,:]
iloc_end_time = time.time()

# Print the time it took to select the rows using .iloc
print("Time using .iloc[]: {} sec".format(iloc_end_time - iloc_start_time))