"""Divvy Up This Exercise
We have pre-loaded an HTML into the string variable html. In this two part problem you will use this html variable as the HTML document to set up a Selector object with, and create a SelectorList which selects all div elements; then, you will check your understanding of what happens within the SelectorList.

Instructions 1
Set up the Selector object sel with the html variable passed as the text argument.
Assign to the variable divs a SelectorList of all div elements within the HTML document."""

from scrapy import Selector

# Create a Selector selecting html as the HTML document
sel = Selector(text=html)

# Create a SelectorList of all div elements in the HTML document
divs = sel.xpath("//div")


"""
Question
Referring to the divs variable you created in the previous exercise, choose the incorrect response.

Possible Answers

divs[2] is a Selector object, which is the third div element in the HTML code.

By chaining, the codedivs[2].xpath('./*') will select all the children of the third div element.

The code len( divs[2].xpath('./*') ) gives the total number of children of the third div element in the HTML code.

divs[2] is another SelectorList of length 2
"""