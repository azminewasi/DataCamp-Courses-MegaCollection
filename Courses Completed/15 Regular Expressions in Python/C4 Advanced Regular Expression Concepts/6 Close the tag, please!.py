"""Close the tag, please!
In the meantime, you are working on one of your other projects. The company is going to develop a new product. It will help developers automatically check the code they are writing. You need to write a short script for checking that every HTML tag that is open has its proper closure.

You have an example of a string containing HTML tags:

<title>The Data Science Company</title>

You learn that an opening HTML tag is always at the beginning of the string. It appears inside <>. A closing tag also appears inside <>, but it is preceded by /.

You also remember that capturing groups can be referenced using numbers, e.g \4.

The list html_tags, containing three strings with HTML tags, and there module are loaded in your session. You can use print() to view the data in the IPython Shell.

Instructions
100 XP
Instructions
100 XP
Complete the regex in order to match closed HTML tags. Find if there is a match in each string of the list html_tags. Assign the result to match_tag.
If a match is found, print the first group captured and saved in match_tag.
If no match is found, complete the regex to match only the text inside the HTML tag. Assign it to notmatch_tag.
Print the first group captured by the regex and save it in notmatch_tag.
"""

for string in html_tags:
    # Complete the regex and find if it matches a closed HTML tags
    match_tag =  re.match(r"<(\w+)>.*?</\1>", string)
 
    if match_tag:
        # If it matches print the first group capture
        print("Your tag {} is closed".format(match_tag.group(1))) 
    else:
        # If it doesn't match capture only the tag 
        notmatch_tag = re.match(r"<(\w+)>", string)
        # Print the first group capture
        print("Close your {} tag!".format(notmatch_tag.group(1)))