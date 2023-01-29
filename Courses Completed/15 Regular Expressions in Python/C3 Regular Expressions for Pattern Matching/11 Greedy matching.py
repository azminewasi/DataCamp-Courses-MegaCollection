"""Greedy matching
Next, you see that numbers still appear in the text of the tweets. So, you decide to find all of them.

Let's imagine that you want to extract the number contained in the sentence I was born on April 24th. A lazy quantifier will make the regex return 2 and 4, because they will match as few characters as needed. However, a greedy quantifier will return the entire 24 due to its need to match as much as possible.

The re module as well as the variable sentiment_analysis are already loaded in your session. You can use print(sentiment_analysis) to view it in the IPython Shell.

Instructions 1/2
50 XP
Instructions 1/2
50 XP
1
Use a lazy quantifier to match all numbers that appear in the variable sentiment_analysis.


Take Hint (-15 XP)
2
Now, use a greedy quantifier to match all numbers that appear in the variable sentiment_analysis."""


# Write a lazy regex expression 
numbers_found_lazy = re.findall(r"[0-9]+?", sentiment_analysis)

# Print out the result
print(numbers_found_lazy)



# Write a greedy regex expression 
numbers_found_greedy = re.findall(r"[0-9]+", sentiment_analysis)

# Print out the result
print(numbers_found_greedy)