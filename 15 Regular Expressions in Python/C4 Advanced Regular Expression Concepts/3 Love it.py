"""Love it!
You are still working on the Twitter sentiment analysis project. First, you want to identify positive tweets about movies and concerts.

You plan to find all the sentences that contain the words love, like, or enjoy and capture that word. You will limit the tweets by focusing on those that contain the words movie or concert by keeping the word in another group. You will also save the movie or concert name.

For example, if you have the sentence: I love the movie Avengers. You match and capture love. You need to match and capture movie. Afterwards, you match and capture anything until the dot.

The list sentiment_analysis containing the text of three tweets and the re module are loaded in your session. You can use print() to view the data in the IPython Shell.

Instructions
100 XP
Instructions
100 XP
Complete the regular expression to capture the words love or like or enjoy. Match and capture the words movie or concert. Match and capture anything appearing until the ..
Find all matches of the regex in each element of sentiment_analysis. Assign them to positive_matches.
Complete the .format() method to print out the results contained in positive_matches for each element in sentiment_analysis.
"""

# Write a regex that matches sentences with the optional words
regex_positive = r"(love|like|enjoy).+?(movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
	# Find all matches of regex in tweet
    positive_matches = re.findall(regex_positive, tweet)
    
    # Complete format to print out the results
    print("Positive comments found {}".format(positive_matches))