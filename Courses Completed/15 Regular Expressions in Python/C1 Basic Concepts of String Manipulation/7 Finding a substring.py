"""Finding a substring
It's a new day at work and you need to continue cleaning your dataset for the movie prediction project. While exploring the dataset, you notice a strange pattern: there are some repeated, consecutive words occurring between the character at position 37 and the character at position 41. You decide to write a function to find out which movie reviews show this peculiarity, remembering that the ending position you specify is not inclusive. If you detect the word, you also want to change the string by replacing it with only one instance of the word.

Complete the if-else statement following the instructions.

The text of three movie reviews has been already saved in the variable movies. You can use print(movies) to view the variable in the IPython Shell.

Instructions

Find if the substring actor occurs between the characters with index 37 and 41 inclusive. If it is not detected, print the statement Word not found.
Replace actor actor with the substring actor if actor occurs only two repeated times.
Replace actor actor actor with the substring actor if actor appears three repeated times."""

for movie in movies:
  	# If actor is not found between character 37 and 41 inclusive
    # Print word not found
    if movie.find("actor", 37, 42) == -1:
        print("Word not found")
    # Count occurrences and replace two with one
    elif movie.count("actor") == 2:  
        print(movie.replace("actor actor", "actor"))
    else:
        # Replace three occurrences with one
        print(movie.replace("actor actor actor", "actor"))