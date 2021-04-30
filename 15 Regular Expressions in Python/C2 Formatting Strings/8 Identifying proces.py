"""Identifying prices
After you showed your report to your boss, he came up with the idea of offering courses to the company's users on some of the tools you studied. In order to make a pilot test, you will send an email offering a course about one of the tools, randomly chosen from your dataset. You also mention that the estimated fee needs to be paid on a monthly basis.

For writing the email, you will use Template strings. You remember that you need to be careful when you use the dollar sign since it is used for identifiers in this case.

For this example, the list tools contains the corresponding tool name, fee and payment type for the product offer. If you want to explore the variable, you can use print() to view it in the IPython Shell.

Instructions
100 XP
Instructions
100 XP
Assign the first, second, and third element of tools to the variables our_tool, our_fee and our_pay respectively.
Complete the template string using $tool, $fee, and $pay as identifiers. Add the dollar sign before the $fee identifier and add the characters ly directly after the $pay identifier.
Substitute identifiers with the three variables you created and print out the results.
"""

# Import template
from string import Template

# Select variables
our_tool = tools[0]
our_fee = tools[1]
our_pay = tools[2]

# Create template
course = Template("We are offering a 3-month beginner course on $tool just for $$ $fee ${pay}ly")

# Substitute identifiers with three variables
print(course.substitute(tool=our_tool, fee=our_fee, pay=our_pay))