Random row selection
In this exercise, you will compare the two methods described for selecting random rows (entries) with replacement in a pandas DataFrame:

The built-in pandas function .random()
The NumPy random integer number generator np.random.randint()
Generally, in the fields of statistics and machine learning, when we need to train an algorithm, we train the algorithm on the 75% of the available data and then test the performance on the remaining 25% of the data.

For this exercise, we will randomly sample the 75% percent of all the played poker hands available, using each of the above methods, and check which method is more efficient in terms of speed.

==================================================================================================================

# Extract number of rows in dataset
N=poker_hands.shape[0]

# Select and time the selection of the 75% of the dataset's rows
rand_start_time = time.time()
poker_hands.iloc[np.random.randint(low=0, high=N, size=int(0.75 * N))]
print("Time using Numpy: {} sec".format(time.time() - rand_start_time))

# Select and time the selection of the 75% of the dataset's rows using sample()
samp_start_time = time.time()
poker_hands.sample(int(0.75 * N), axis=0, replace = True)
print("Time using .sample: {} sec".format(time.time() - samp_start_time))