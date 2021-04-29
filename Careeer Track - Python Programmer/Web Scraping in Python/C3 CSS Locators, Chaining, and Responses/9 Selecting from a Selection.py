"""Selecting from a Selection
In this exercise, you will find the text from an h4 element within a particular div element. It will occur in steps where the first step is selecting a family of div elements, and the second step is narrowing in on the first one, from which we will grab the h4 element text. This process of progressively narrowing in on elements (e.g., first to the div elements, then to the h4 element) is another example of "chaining", even if it doesn't look exactly the same as we've seen it before.

Along the way in this exercise, there is a variable first_div set up for you to use. Think carefully about what type of object first_div is!"""


"""Assign to the variable divs a SelectorList which selects all div elements belonging to the class course-block.
Assign to the variable h4_text the text from the only h4 element within the content selected in first_div. Since we only want the text from the single element we will select, we use the extract_first() method to extract the text."""

# Select all desired div elements
divs = response.css('div.course-block')

# Take the first div element
first_div = divs[0]

# Extract the text from the (only) h4 element in first_div
h4_text = first_div.css('h4::text').extract_first()

# Print out the text
print( "The text from the h4 element is:", h4_text )




"""We defined the object first_div in the last part of this question. What type of element is first_div?
Possible Answers

Another Response object.

A Selector object.

An extracted string from the data of a selected div element."""