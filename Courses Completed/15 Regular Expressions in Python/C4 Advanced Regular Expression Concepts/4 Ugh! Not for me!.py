"""Ugh! Not for me!
After finding positive tweets, you want to do it for negative tweets. Your plan now is to find sentences that contain the words hate, dislike or disapprove. You will again save the movie or concert name. You will get the tweet containing the words movie or concert but this time, you don't plan to save the word.

For example, if you have the sentence: I dislike the movie Avengers a lot.. You match and capture dislike. You will match but not capture the word movie. Afterwards, you match and capture anything until the dot.

The list sentiment_analysis containing the text of three tweets as well as the re module are loaded in your session. You can use print() to view the data in the IPython Shell.

Instructions
100 XP
Instructions
100 XP
Complete the regular expression to capture the words hate or dislike or disapprove. Match but don't capture the words movie or concert. Match and capture anything appearing until the ..
Find all matches of the regex in each element of sentiment_analysis. Assign them to negative_matches.
Complete the .format() method to print out the results contained in negative_matches for each element in sentiment_analysis."""

# Write a regex that matches sentences with the optional words
regex_negative = r"(hate|dislike|disapprove).+?(?:movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
	# Find all matches of regex in tweet
    negative_matches = re.findall(regex_negative, tweet)
    
    # Complete format to print out the results
    print("Negative comments found {}".format(negative_matches))