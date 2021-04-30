"""Are they bots?
The company that you are working for asked you to perform a sentiment analysis using a dataset with tweets. First of all, you need to do some cleaning and extract some information.
While printing out some text, you realize that some tweets contain user mentions. Some of these mentions follow a very strange pattern. A few examples that you notice: @robot3!, @robot5& and @robot7#

To analyze if those users are bots, you will do a proof of concept with one tweet and extract them using the .findall() method.

You write down some helpful metacharacters to help you later:

\d: digit
\w: word character
\W: non-word character
\s: whitespace

The text of one tweet was saved in the variable sentiment_analysis. You can use print(sentiment_analysis) to view it in the IPython Shell.

Instructions
Import the re module.
Write a regex that matches the user mentions that starts with @ and follows the pattern, e.g. @robot3!.
Find all the matches of the pattern in the sentiment_analysis variable."""

# Import the re module
import re

# Write the regex
regex = r"@robot\d\W"

# Find all matches of regex
print(re.findall(regex, sentiment_analysis))