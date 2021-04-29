"""
Artificial reviews
While checking out the movie reviews in your dataset, you realize that some of them show an atypical pattern. Since you should only include true reviews in your analysis, you decide to extract the suspicious ones that follow this pattern. You want to see if it is possible to artificially create reviews by using the first and last part of one example review and changing a keyword in the middle.

The text of two movie reviews has been already saved in the variables movie1 and movie2. You can use the print() function to view the variables in the IPython Shell.

Remember: The 1st character of a string has index 0.
"""

# Select the first 32 characters of movie1
first_part = movie1[:32]

# Select from 43rd character to the end of movie1
last_part = movie1[42:]

# Select from 33rd to the 42nd character
middle_part = movie2[32:42]

# Print concatenation and movie2 variable
print(first_part+middle_part+last_part) 
print(movie2)