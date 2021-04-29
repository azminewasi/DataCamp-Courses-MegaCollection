"""Responding with Selectors
Something that we should emphasize at this point about the relationship between a Selector and Response objects is that both objects return a SelectorList when using the xpath or css methods to direct to elements. In this exercise, we'll prove it to you, by having you find all hyperlink elements belonging to the class course-block__link (notice the double underscore!) and looking at the object that is produced when doing so.

Recall that to find an element by class, you can use a period (.). For example, div.class-2 selects all div elements belonging to class-2.

We have pre-loaded both a Response object named response and a Selector object named sel with the content from the same "secret" website. Once you complete the task of creating a CSS Locator, you will compare both the output from response.css and selector.css to see that they are effectively the same!

Instructions

Assign to the variable css_locator a CSS Locator string which directs to all hyperlink a elements belonging to the class course-block__link.
Assign to the variable response_as the output of passing the css_locator variable to the css method in response.
Assign to the variable sel_as the output of passing the css_locator variable to the css method in sel."""

# Create a CSS Locator string to the desired hyperlink elements
css_locator = 'a.course-block__link'

# Select the hyperlink elements from response and sel
response_as = response.css(css_locator)
sel_as = sel.css(css_locator)

# Examine similarity
nr = len( response_as )
ns = len( sel_as )
for i in range( min(nr, ns, 2) ):
  print( "Element %d from response: %s" % (i+1, response_as[i]) )
  print( "Element %d from sel: %s" % (i+1, sel_as[i]) )
  print( "" )