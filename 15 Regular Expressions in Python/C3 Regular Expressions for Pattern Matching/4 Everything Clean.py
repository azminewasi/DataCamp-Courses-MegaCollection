"""Everything clean
Back to your Twitter sentiment analysis project! There are several types of strings that increase your sentiment analysis complexity. But these strings do not provide any useful sentiment. Among them, we can have links and user mentions.

In order to clean the tweets, you want to extract some examples first. You know that most of the times links start with http and do not contain any whitespace, e.g. https://www.datacamp.com. User mentions start with @ and can have letters and numbers only, e.g. @johnsmith3.

You write down some helpful quantifiers to help you: * zero or more times, + once or more, ? zero or once.

The list sentiment_analysis containing the text of three tweet are already loaded in your session. You can use print() to view the data in the IPython Shell.

Instructions
Import the re module.
Write a regex to find all the matches of http links appearing in each tweet in sentiment_analysis. Print out the result.
Write a regex to find all the matches of user mentions appearing in each tweet in sentiment_analysis. Print out the result.
"""

# Import re module
import re

for tweet in sentiment_analysis:
  	# Write regex to match http links and print out result
	print(re.findall(r"http\S+", tweet))

	# Write regex to match user mentions and print out result
	print(re.findall(r"@\w+", tweet))