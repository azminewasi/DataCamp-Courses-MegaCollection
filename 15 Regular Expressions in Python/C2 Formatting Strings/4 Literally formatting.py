"""Literally formatting
While analyzing the text from Wikipedia pages, you read that Python 3.6 introduced f-strings.

You remember that you've created a website that displayed data science facts but it was too slow. You think that it could be due to the string formatting you used. Because f-strings are very fast and easy to use, you decide to rewrite that project.

The variables field1, field2 and field3 containing character strings as well as the numeric variables fact1, fact2, fact3 and fact4 have been saved.

If you want to explore the variables, you can use print() to view them in the IPython Shell."""

# Complete the f-string
print(f"Data science is considered {field1!r} in the {fact1:d}st century")

# Complete the f-string
print(f"About {fact2:5e} of {field2} in the world")


# Complete the f-string
print(f"{field3} create around {fact3:.2f}% of the data but only {fact4:.1f}% is analyzed")