"""Taking one element
Let's start using data from the Dask bag speeches of State of the Union addresses. For large datasets, the .take() method is useful for inspecting data & data types while processing dask bags. The value returned by .take(n) is a tuple of the first n elements of the dask.bag.

The speeches bag from the previous exercise is provided for you. Your task is to extract the first element of the bag using .take(), to determine its datatype, and to print the words of the first speech.

Instructions
Invoke .take(1) from speeches and assign the result to one_element.
Extract the first element of one_element and assign it to first_speech.
Print the type of first_speech.
Print the first 60 characters of first_speech."""

# Call .take(1): one_element
one_element = speeches.take(1)

# Extract first element of one_element: first_speech
first_speech = one_element[0]

# Print type of first_speech and first 60 characters
print(type(first_speech))
print(first_speech[:60])