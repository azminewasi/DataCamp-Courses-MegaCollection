"""Find the numbers
While examining the tweet text in your dataset, you detect that some tweets carry more information. The text contains the number of retweets, user mentions, and likes. You decide to extract this important information that is given as in this example:

Agh,snow! User_mentions:9, likes: 5, number of retweets: 4

You pull a list of metacharacters:\d digit,\w word character,\s whitespace.

Always indicate whitespace with metacharacters.

The variable sentiment_analysis containing the text of one tweet and the re module were loaded in your session. You can use print() to view it in the IPython Shell.

Instructions 1/3
35 XP
Instructions 1/3
35 XP
1
Write a regex that matches the number of user mentions given as, for example, User_mentions:9 in sentiment_analysis.


Take Hint (-10 XP)
2
Write a regex that matches the number of likes given as, for example, likes: 5 in sentiment_analysis.

3
Write a regex that matches the number of retweets given as, for example, number of retweets: 4 in sentiment_analysis."""

# Write a regex to obtain number of retweets
print(re.findall(r"number\sof\sretweets:\s\d", sentiment_analysis))