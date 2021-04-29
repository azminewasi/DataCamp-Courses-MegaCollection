"""Replacing negations
In order to keep working with your prediction project, your next task is to figure out how to handle negations that occur in your dataset. Some algorithms for prediction do not work well with negations, so a good way to handle this is to remove either not or n't, and to replace the next word by its antonym.

Let's imagine that you have the string: The movie isn't good. You will need to remove n't and replace good for bad. This way, your string ends up being The movie is bad. You notice that in the first column of the dataset, you have a string that uses the word isn't followed by important.

The text of this column has been already saved in the variable movies so you start working with it. You can use print(movies) to view it in the IPython Shell.

Instructions
Replace the substring isn't with the word is.
Replace the substring important with the word insignificant.
Print out the result contained in the variable movies_antonym."""

# Replace negations 
movies_no_negation = movies.replace("isn't", "is")

# Replace important
movies_antonym = movies_no_negation.replace("important", "insignificant")

# Print out
print(movies_antonym)