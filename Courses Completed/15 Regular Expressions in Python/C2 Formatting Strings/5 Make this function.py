"""Make this function
Wow! You are excited to see how fast and easy f-strings worked. So you plan to rewrite some more of your old code.

Now you know that f-strings allow you to evaluate expressions where they appear and include function and method calls. You decide to use them in a project where you analyze 120 tweets to check if they include links to different news. In that way, you expect the code to be cleaner and more readable.

The variables number1, number2,string1, and list_links have already been pre-loaded.

If you want to explore the variables, you can use print() to view them in the IPython Shell.

Instructions 1/3
35 XP
Instructions 1/3
35 XP
Inside the f-string, include number1,number2 and the result of dividing number1 by number2 rounded to one decimal.

2
Inside the f-string, use .replace() to replace the substring https with an empty substring in string1.

3
Inside the f-string, get list_links length, multiply it by 100 and divide it by 120. Round the result to two decimals."""

# Include both variables and the result of dividing them 
print(f"{number1} tweets were downloaded in {number2} minutes indicating a speed of {number1/number2:0.1f} tweets per min")

# Replace the substring https by an empty string
print(f"{string1.replace('https','')}")

# Divide the length of list by 120 rounded to two decimals
print(f"Only {len(list_links)*100/120:0.2f}% of the posts contain links")