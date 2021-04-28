Column selection: .iloc[] vs by name
In the previous exercise, you saw how the .loc[] and .iloc[] functions can be used to locate specific rows of a DataFrame (based on the index). Turns out, the .iloc[] function performs a lot faster (~ 2 times) for this task!

Another important task is to find the faster function to select the targeted features (columns) of a DataFrame. In this exercise, we will compare the following:

using the index locator .iloc()
using the names of the columns While we can use both functions to perform the same task, we are interested in which is the most efficient in terms of speed.
In this exercise, you will continue working with the poker data which is stored in poker_hands. Take a second to examine the structure of this DataFrame by calling poker_hands.head() in the console!

Instructions 
3
Use the .iloc indexer to select the first, third, fourth, sixth and seventh column ('S1', 'S2', 'R2', 'R3', 'S4') of the DataFrame poker_hands by their index and find the time it took.

==================================================================================================================

# Use .iloc to select the first, fourth, fifth, seventh and eighth column and record the times before and after
iloc_start_time = time.time()
cols = poker_hands.iloc[:,[0,3,4,6,7]]
iloc_end_time = time.time()

# Print the time it took
print("Time using .iloc[] : {} sec".format(iloc_end_time - iloc_start_time))

# Use simple column selection to select the first, fourth, fifth, seventh and eighth column and record the times before and after
names_start_time = time.time()
cols = poker_hands[['S1', 'S2', 'R2', 'R3', 'S4']]
names_end_time = time.time()

# Print the time it took
print("Time using selection by name : {} sec".format(names_end_time - names_start_time))