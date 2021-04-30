"""Getting tokens
Your next step is to tokenize the text of your tweets. Tokenization is the process of breaking a string into lexical units or, in simpler terms, words. But first, you need to remove hashtags so they do not cloud your process. You realize that hashtags start with a # symbol and contain letters and numbers but never whitespace. After that, you plan to split the text at whitespace matches to get the tokens.

You bring your list of quantifiers to help you: * zero or more times, + once or more, ? zero or once, {n, m} minimum n, maximum m.

The variable sentiment_analysis containing the text of one tweet as well as the re module are already loaded in your session. You can use print(sentiment_analysis) to view it in the IPython Shell."""

regex = r"#\w+"

# Write a regex matching the hashtag pattern
regex = r"#\w+"

# Replace the regex by an empty string
no_hashtag = re.sub(regex, "", sentiment_analysis)

# Write a regex matching the hashtag pattern
regex = r"#\w+"

# Replace the regex by an empty string
no_hashtag = re.sub(regex, "", sentiment_analysis)

# Get tokens by splitting text
print(re.split(r"\s+", no_hashtag))