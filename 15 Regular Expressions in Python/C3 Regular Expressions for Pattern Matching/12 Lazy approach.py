""""Lazy approach
You have done some cleaning in your dataset but you are worried that there are sentences encased in parentheses that may cloud your analysis.

Again, a greedy or a lazy quantifier may lead to different results.

For example, if you want to extract a word starting with a and ending with e in the string I like apple pie, you may think that applying the greedy regex a.+e will return apple. However, your match will be apple pie. A way to overcome this is to make it lazy by using ? which will return apple.

The re module and the variable sentiment_analysis are already loaded in your session.

Instructions 1/2
50 XP
Instructions 1/2
50 XP
1
Use a greedy quantifier to match text that appears within parentheses in the variable sentiment_analysis.


Take Hint (-15 XP)
2
Now, use a lazy quantifier to match text that appears within parentheses in the variable sentiment_analysis.""""

# Write a greedy regex expression to match 
sentences_found_greedy = re.findall(r"\(.*\)", sentiment_analysis)

# Print out the result
print(sentences_found_greedy)

# Write a lazy regex expression
sentences_found_lazy = re.findall(r"\(.*?\)", sentiment_analysis)

# Print out the results
print(sentences_found_lazy)