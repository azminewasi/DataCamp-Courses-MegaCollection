"""ry another name
You are still working on your Twitter sentiment analysis. You analyze now some things that caught your attention. You noticed that there are email addresses inserted in some tweets. Now, you are curious to find out which is the most common name.

You want to extract the first part of the email. E.g. if you have the email marysmith90@gmail.com, you are only interested in marysmith90.
You need to match the entire expression. So you make sure to extract only names present in emails. Also, you are only interested in names containing upper (e.g. A,B, Z) or lowercase letters (e.g. a, d, z) and numbers.

The list sentiment_analysis containing the text of three tweets as well as the re module were loaded in your session. You can use print() to view it in the IPython Shell.

Instructions
100 XP
Instructions
100 XP
Complete the regex to match the email capturing only the name part. The name part appears before the @.
Find all matches of the regex in each element of sentiment_analysis analysis. Assign it to the variable email_matched.
Complete the .format() method to print the results captured in each element of sentiment_analysis analysis."""

# Write a regex that matches email
regex_email = r"([A-Za-z0-9]+)@\S+"

for tweet in sentiment_analysis:
    # Find all matches of regex in each tweet
    email_matched = re.findall(regex_email, tweet)

    # Complete the format method to print the results
    print("Lists of users found in this tweet: {}".format(email_matched))