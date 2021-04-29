"""Inheriting the Spider
When learning about scrapy spiders, we saw that the main portion of the code for us to adjust is the class for the spider. To help build some familiarity of the class, you will complete a short piece of code to complete a toy-model of the spider class code. We've omitted the code that would actually run the spider, only including the pieces necessary to create the class.

As mentioned in the lesson, a class is roughly a collection of related variables and functions housed together. Sometimes one class likes to use methods from another class, and so we will inherit methods from a different class. That's what we do in the spider class.

We wrote the function inspect_class to look at the your class once you're done, if you'd like to test your solution!

Instructions
Pass scrapy.Spider as an argument to the class YourSpider; this will make it so that YourSpider inherits the methods from scrapy.Spider."""

# Import scrapy library
import scrapy

# Create the spider class
class YourSpider(scrapy.Spider):
  name = "your_spider"
  # start_requests method
  def start_requests(self):
    pass
  # parse method
  def parse(self, response):
    pass
  
# Inspect Your Class
inspect_class(YourSpider)