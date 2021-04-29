"""Requesting a Selector
We have pre-loaded the URL for a particular website in the string variable url and use the requests library to put the content from the website into the string variable html. Your task is to create a Selector object sel using the HTML source code stored in html.

Instructions
100 XP
Fill in the two blanks below to assign to create the Selector object sel which uses the string html as the text it inputs."""

# Import a scrapy Selector
from scrapy import Selector

# Import requests
import requests

# Create the string html containing the HTML source
html = requests.get( url ).content

# Create the Selector object sel from html
sel = Selector(text=html)

# Print out the number of elements in the HTML document
print( "There are 1020 elements in the HTML document.")
print( "You have found: ", len( sel.xpath('//*') ) )