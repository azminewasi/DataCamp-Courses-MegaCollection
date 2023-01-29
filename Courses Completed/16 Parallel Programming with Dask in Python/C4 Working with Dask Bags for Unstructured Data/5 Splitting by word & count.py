"""Splitting by word & count
Using the speeches bag from earlier exercises let's examine some statistics about the State of the Union addresses.

Your job is to split each speech into a list of words using a single space ' ' as the separator. At this point the Dask Bag can be considered a list-of-lists. You'll then map the len() function over each of the inner lists to compute the number of words in each speech and then compute the mean() of the lengths to get the average word count.

Instructions
Call .str.split(' ') on speeches and assign it to by_word.
Map the len function over by_word and assign it to n_words.
Call .mean() and assign it to avg_words.
Print the type of avg_words and the value of avg_words.compute()."""

# Call .str.split(' ') from speeches and assign it to by_word
by_word = speeches.str.split(' ')

# Map the len function over by_word and compute its mean
n_words = by_word.map(len)
avg_words = n_words.mean()

# Print the type of avg_words and value of avg_words.compute()
print(type(avg_words))
print(avg_words.compute())