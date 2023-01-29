"""NumPy transformations
Many NumPy transformations, while fast, use one or more temporary arrays. Therefore, those transformations require more storage than the original array required.

An array of temperature values in Celsius is provided for you as celsius. Your job is to monitor memory consumption while applying NumPy vectorized operations. The data comes from The Weather Underground.

The function memory_footprint() has been provided for you to return the total amount of memory (in megabytes or MB) currently in use by your program. This function uses the psutil and os modules. You can find the function definition in the course appendix.

Instructions
Print the size in MB of the celsius array by dividing its nbytes attribute by 1024**2.
Call memory_footprint() and save the result to before.
Convert celsius to fahrenheit by multiplying by 9/5 and adding 32.
Call memory_footprint(), save the result to after, and then print the difference between after and before."""

# Print the size in MB of the celsius array
print(celsius.nbytes/1024**2)

# Call memory_footprint(): before
before=memory_footprint()

# Convert celsius by multiplying by 9/5 and adding 32: fahrenheit
fahrenheit=(celsius*9/5)+32

# Call memory_footprint(): after
after=memory_footprint()

# Print the difference between after and before
print(after - before)