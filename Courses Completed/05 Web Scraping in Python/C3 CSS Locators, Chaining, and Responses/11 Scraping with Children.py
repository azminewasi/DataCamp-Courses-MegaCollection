"""Scraping with Children
We did a cute trick in the lesson to calculate how many children there were of one of the div elements belonging to the class course-block. Here we ask you to find the number of children of a mystery element (already stored within a Selector object, so you can use the xpath or css method).

To be explicit, we have created the Selector object mystery in the following way:

We first loaded a Response variable using a secret website as the input.
Then we used a call to the xpath method to create a SelectorList of elements (but we won't say which ones)
Finally, we let mystery be the first Selector object of this SelectorList.


Scraping with Children
Fill in the blank below to chain on a call to xpath so that we can calculate the number of children of the mystery element; we assign this number to the variable how_many_kids.

Remember, if you use xpath, this really is an instance of chaining, so don't forget to use a period (.) as glue

"""

# Calculate the number of children of the mystery element
how_many_kids = len( mystery.xpath("./*") )

# Print out the number
print( "The number of elements you selected was:", how_many_kids )