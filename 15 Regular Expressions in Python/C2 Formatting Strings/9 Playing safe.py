"""Playing safe
You are in charge of a new project! Your job is to start collecting information from the company's main application users. You will make an online quiz and ask your users to voluntarily answer two questions. However, it is not mandatory for the user to answer both. You will be handling user-provided strings so you decide to use the Template method to print the input information. This allows users to double-check their answers before submitting them.

The answer of one user has been stored in the dictionary answers. You can use the print() function to view the variables in the IPython Shell.

Instructions 1/3
35 XP
1
Complete the template string using $answer1 and $answer2 as identifiers.


Take Hint (-10 XP)
2
Use the method .substitute() to replace the identifiers with the values in answers in the predefined template.

3
Use the method .safe_substitute() to replace the identifiers with the values in answers in the predefined template."""

# Import template
from string import Template

# Complete template string using identifiers
the_answers = Template("Check your answer 1: $answer1, and your answer 2: $answer2")

# Use safe_substitute to replace identifiers
try:
    print(the_answers.safe_substitute(answers))
except KeyError:
    print("Missing information")