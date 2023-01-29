'''
First day!
Congratulations! It's your first day as a data scientist in the company! Your first project is to build a model for predicting if a movie will get a positive or negative review.
You need to start exploring your dataset. In order to create a function that will scan each movie review, you want to know how many characters every string has and print the result out together with a statement that indicate what the number refers to. To test if your function works correctly, you are going to start by analyzing only one example.

The text of one movie review has been already saved in the variable movie. You can use print(movie) to view the variable in the IPython Shell.
'''


# Find characters in movie variable
length_string = len(movie)

# Convert to string
to_string = str(length_string)

# Predefined variable
statement = "Number of characters in this review:"

# Concatenate strings and print result
print(statement+" "+to_string)