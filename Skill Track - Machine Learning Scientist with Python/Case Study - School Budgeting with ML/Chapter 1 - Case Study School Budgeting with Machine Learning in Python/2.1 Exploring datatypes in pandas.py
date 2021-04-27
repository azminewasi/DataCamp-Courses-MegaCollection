Exploring datatypes in pandas
It's always good to know what datatypes you're working with, especially when the inefficient pandas type object may be involved. Towards that end, let's explore what we have.

The data has been loaded into the workspace as df. Your job is to look at the DataFrame attribute .dtypes in the IPython Shell, and call its .value_counts() method in order to answer the question below.

Make sure to call df.dtypes.value_counts(), and not df.value_counts()! Check out the difference in the Shell. df.value_counts() will return an error, because it is a Series method, not a DataFrame method.

How many columns with dtype object are in the data?

Instructions
50 XP
Instructions
50 XP
Possible Answers

2.

23.

64.

25.




In [1]:
df.dtypes.value_counts()
Out[1]:

object     23
float64     2
dtype: int64



23