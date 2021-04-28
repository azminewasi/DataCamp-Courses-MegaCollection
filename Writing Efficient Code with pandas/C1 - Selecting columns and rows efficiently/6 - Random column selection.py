Random column selection
In the previous exercise, we examined two ways to select random rows from a pandas DataFrame. We can use the same functions to randomly select columns in a pandas DataFrame.

To randomly select 4 columns out of the poker dataset, you will use the following two functions:

The built-in pandas function .random()
The NumPy random integer number generator np.random.randint()

==================================================================================================================

# Extract number of columns in dataset
D=poker_hands.shape[1]

# Select and time the selection of 4 of the dataset's columns using NumPy
np_start_time = time.time()
poker_hands.iloc[:,np.random.randint(low=0, high=D, size=4)]
print("Time using NymPy's random.randint(): {} sec".format(time.time() - np_start_time))

# Select and time the selection of 4 of the dataset's columns using pandas
pd_start_time = time.time()
poker_hands.sample(4, axis=1)
print("Time using panda's .sample(): {} sec".format(time.time() - pd_start_time))