'''
Setting and removing indexes
pandas allows you to designate columns as an index. This enables cleaner code when taking subsets (as well as providing more efficient lookup under some circumstances).

In this chapter, you'll be exploring temperatures, a DataFrame of average temperatures in cities around the world. pandas is loaded as pd.

Instructions
Look at temperatures.
Set the index of temperatures to "city", assigning to temperatures_ind.
Look at temperatures_ind. How is it different from temperatures?
Reset the index of temperatures_ind, keeping its contents.
Reset the index of temperatures_ind, dropping its contents.
'''

# Look at temperatures
print(temperatures)

# Index temperatures by city
temperatures_ind = temperatures.set_index("city")

# Look at temperatures_ind
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop=True))