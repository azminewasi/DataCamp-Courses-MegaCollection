"""Match and split
Some of the tweets in your dataset were downloaded incorrectly. Instead of having spaces to separate words, they have strange characters. You decide to use regular expressions to handle this situation. You print some of these tweets to understand which pattern you need to match.

You notice that the sentences are always separated by a special character, followed by a number, the word break, and after that, another special character, e.g &4break!. The words are always separated by a special character, the word new, and a normal random character, e.g #newH.

The variable sentiment_analysis containing the text of one tweet, as well as the re module were already loaded in your session. You can use print(sentiment_analysis) to view it in the IPython Shell."""

"""Write a regex that matches the pattern separating the sentences in sentiment_analysis, e.g. &4break!"""
# Write a regex to match pattern separating sentences
regex_sentence = r"\W\dbreak\W"

"""Replace regex_sentence with a space " " in the variable sentiment_analysis. Assign it to sentiment_sub."""
# Write a regex to match pattern separating sentences
regex_sentence = r"\W\dbreak\W"

# Replace the regex_sentence with a space
sentiment_sub = re.sub(regex_sentence, " ", sentiment_analysis)
"""
Write a regex that matches the pattern separating the words in sentiment_analysis, e.g. #newH."""
# Write a regex to match pattern separating words
regex_words = r"\Wnew\w"

"""Replace regex_words with a space in the variable sentiment_sub. Assign it to sentiment_final and print out the result."""

# Replace the regex_words and print the result
sentiment_final = re.sub(regex_words, " ", sentiment_sub)
print(sentiment_final)