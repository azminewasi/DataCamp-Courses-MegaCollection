"""Finding files
You are not satisfied with your tweets dataset cleaning. There are still extra strings that do not provide any sentiment. Among them are strings that refer to text file names.

You also find a way to detect them:

They appear at the start of the string.
They always start with a sequence of 2 or 3 upper or lowercase vowels (a e i o u).
They always finish with the txt ending.
You are not sure if you should remove them directly. So you write a script to find and store them in a separate dataset.

You write down some metacharacters to help you: ^ anchor to beginning, . any character.

The variable sentiment_analysis containing the text of two tweets as well as the re module are already loaded in your session. You can use print() to view it in the IPython Shell.

Instructions
100 XP
Instructions
100 XP
Write a regex that matches the pattern of the text file names, e.g. aemyfile.txt.
Find all matches of the regex in the elements of sentiment_analysis. Print out the result.
Replace all matches of the regex with an empty string "". Print out the result."""

# Write a regex to match text file name
regex = r"^[aeiouAEIOU]{2,3}.+txt"

for text in sentiment_analysis:
	# Find all matches of the regex
	print(re.findall(regex, text))
    
	# Replace all matches with empty string
	print(re.sub(regex, "", text))