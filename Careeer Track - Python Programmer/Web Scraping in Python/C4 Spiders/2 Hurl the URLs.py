"""Hurl the URLs
In the next lesson we will talk about the start_requests method within the spider class. In this quick exercise, we ask you to change around a variable within the start_requests method which foreshadows some of what we will be learning in the next lesson. Basically, we want you to start becoming comfortable turning some of the wheels within a spider class; in this case, making a list of urls within the start_requests method.

We've written a function inspect_class which will print out the list of elements you have in the urls variable within the start_requests method.

Note: in the next several exercises, you will write code to complete your spider class, but the code does not yet include the pieces to actually run the spider; that will come at the end.

Instructions
Fill in the blank within the start_requests method to assign the variable urls a list with the two strings: "https://www.datacamp.com" and"https://scrapy.org"."""

# Import scrapy library
import scrapy

# Create the spider class
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    urls = ["https://www.datacamp.com","https://scrapy.org"]
    for url in urls:
      yield url
  # parse method
  def parse( self, response ):
    pass
  
# Inspect Your Class
inspect_class( YourSpider )