"""You've been `href`ed
In a previous exercise, you created a CSS Locator string to select the hyperlink (a element) children of all div elements belonging to the class "course-block". Here we have created a SelectorList called course_as having selected those hyperlink children.

Now, we want you to fill in the blank below to extract the href attribute values from these elements. This is another example of chaining, as we've seen in a previous exercise.

The point here is that we can chain together calls to the methods css and xpath, and combine them! We help nudge you in the correct direction by giving you the solution if we chain with another call to the css method.

Instructions
100 XP
Instructions
100 XP
Set up the Selector object sel using the string html as the text input.
Assign to the variable hrefs_from_xpath the href attribute values from the elements in course_as. Your solution should match hrefs_from_css!"""
from scrapy import Selector

# Create a selector object from a secret website
sel = Selector( text = html )

# Select all hyperlinks of div elements belonging to class "course-block"
course_as = sel.css( 'div.course-block > a' )

# Selecting all href attributes chaining with css
hrefs_from_css = course_as.css( '::attr(href)' )

# Selecting all href attributes chaining with xpath
hrefs_from_xpath = course_as.xpath( './@href' )