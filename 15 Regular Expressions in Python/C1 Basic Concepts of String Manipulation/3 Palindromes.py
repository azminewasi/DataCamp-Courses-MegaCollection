"""
Palindromes
Next, you are committed to find any peculiarity in the words included in the movie review dataset. A palindrome is a sequence of characters which can be read the same backward as forward, for example: Madam or No lemon, no melon. You realize that there are some funny movie names that can have this characteristic. You want to make a list of all movie titles that are funny palindromes but you will start by analyzing one example.

In python, you can also specify steps by using a third index. If you don't specify the first or second index and the third one is negative, it will return the characters jumping and backwards.

The text of a movie review for one example has been already saved in the variable movie. You can use print(movie) to view the variable in the IPython Shell.

Extract the substring from the 12th to the 30th character from the variable movie which corresponds to the movie title. Store it in the variable movie_title.
Get the palindrome by reversing the string contained in movie_title.
Complete the code to print out the movie_title if it is a palindrome.
"""
# Get the word
movie_title = movie[11:30]

# Obtain the palindrome
palindrome = movie_title[::-1]

# Print the word if it's a palindrome
if movie_title == palindrome:
	print(movie_title)