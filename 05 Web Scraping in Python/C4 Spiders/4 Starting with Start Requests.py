"""Starting with Start Requests
In the last lesson we learned about setting up the start_requests method within a scrapy spider. Here we have another toy-model spider which doesn't actually scrape anything, but gives you a chance to play with the start_requests method. What we want is for you to start becomming familiar with the arguments you pass into the scrapy.Request call within start_requests.

As before, we have created the function inspect_class to examine what you are yielding in start_requests.

Instructions
Fill in the required scrapy object into the class YourSpider needed to create the scrapy spider.
Fill in the blank in the yielded scrapy.Request call within the start_requests method so that the URL this spider would start scraping is "https://www.datacamp.com" and would use the parse method (within the YourSpider class) as the method to parse the website.
"""

# Import scrapy library
import scrapy

# Create the spider class
class YourSpider(scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url="https://www.datacamp.com", callback=self.parse )
  # parse method
  def parse( self, response ):
    pass
  
# Inspect Your Class
inspect_class( YourSpider )