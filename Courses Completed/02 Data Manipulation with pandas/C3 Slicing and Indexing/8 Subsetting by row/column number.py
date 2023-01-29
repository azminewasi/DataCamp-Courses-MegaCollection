'''Subsetting by row/column number
The most common ways to subset rows are the ways we've previously discussed: using a Boolean condition or by index labels. However, it is also occasionally useful to pass row numbers.

This is done using .iloc[], and like .loc[], it can take two arguments to let you subset by rows and columns.

pandas is loaded as pd. temperatures (without an index) is available.

Instructions
100 XP
Instructions
100 XP
Use .iloc[] on temperatures to take subsets.

Get the 23rd row, 2nd column (index positions 22 and 1).
Get the first 5 rows (index positions 0 to 5).
Get all rows, columns 3 and 4 (index positions 2 to 4).
Get the first 5 rows, columns 3 and 4.
'''
# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22, 1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[:5])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:, 2:4])

# Use slicing in both directions at once
print(temperatures.iloc[:5, 2:4])