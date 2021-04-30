"""Some time ago
You are interested in knowing when the tweets were posted. After reading a little bit more, you learn that dates are provided in different ways. You decide to extract the dates using .findall() so you can normalize them afterwards to make them all look the same.

You realize that the dates are always presented in one of the following ways:

27 minutes ago

4 hours ago

23rd june 2018

1st september 2019 17:25

The list sentiment_analysis containing the text of three tweets, as well as the re module are already loaded in your session. You can use print() to view the data in the IPython Shell.

Instructions 1/3
35 XP
Instructions 1/3
35 XP
1
Complete the for-loop with a regex that finds all dates in a format similar to 27 minutes ago or 4 hours ago.


Take Hint (-10 XP)
2
Complete the for-loop with a regex that finds all dates in a format similar to 23rd june 2018.

3
Complete the for-loop with a regex that finds all dates in a format similar to 1st september 2019 17:25."""

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\s\w+\sago", date))


    # Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}", date))

    # Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}\s\d{1,2}:\d{2}", date))