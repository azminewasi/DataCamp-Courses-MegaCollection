"""Get an "a" in this Course
We have loaded the HTML from a secret website which you will use to set up a Selector object and the function how_many_elements(). When passing this function a CSS Locator string, it will print out the number of elements that the CSS Locator you wrote has selected.

In the second part of this problem, we want you to create a CSS Locator string which will select a certain collection of elements as described here: Select the hyperlink (a element) children of all div elements belonging to the class "course-block" (that is, any div element with a class attribute such that "course-block" is one of the classes assigned). The number of such elements is 11, so you can check your solution with how_many_elements if you choose."""









from scrapy import Selector

# Create a selector from the html (of a secret website)
sel = Selector( text = html )

# Fill in the blank
css_locator = "div.course-block>a"

# Print the number of selected elements.
how_many_elements( css_locator )