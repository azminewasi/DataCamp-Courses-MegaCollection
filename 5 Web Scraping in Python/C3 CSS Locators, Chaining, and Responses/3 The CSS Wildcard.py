"""The CSS Wildcard
You can use the wildcard * in CSS Locators too! In fact, we can use it in a similar way, when we want to ignore the tag type. For example:

The CSS Locator string '*' selects all elements in the HTML document.
The CSS Locator string '*.class-1' selects all elements which belong to class-1, but this is unnecessary since the string '.class-1' will also do the same job.
The CSS Locator string '*#uid' selects the element with id attribute equal to uid, but this is unnecessary since the string '#uid' will also do the same job.
In this exercise, we want you to work by analogy with the wildcard character you know from XPath notation to discover how to select all the children of a certain element in CSS Locator notation.

Instructions
100 XP
Assign to the variable css_locator a CSS Locator string which will select all children (regardless of tag-type) of the unique element in the HTML document that has its id attribute equal to uid.
"""

# Create the CSS Locator to all children of the element whose id is uid
css_locator = "#uid > *"