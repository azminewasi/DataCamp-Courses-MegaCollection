"""Self Referencing is Classy
You probably have noticed that within the spider class, we always input the argument self in the start_requests and parse methods (just look in the sample code in this exercise!). This allows us to reference between methods within the class. That is, if we want to refer to the method parse within the start_requests method, we would need to write self.parse rather than just parse; what writing self does is tell the code: "Look in the same class as start_requests for a method called parse to use."

In this exercise you will get a chance to play with this "self referencing".

Instructions
Fill in the required scrapy object into the class YourSpider needed to create the scrapy spider.
Pass the string argument "Hello World!" to fill in the blank in the start_requests method to use the print_msg method."""

# Import scrapy library
import scrapy

# Create the spider class
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    self.print_msg( "Hello World!" )
  # parse method
  def parse( self, response ):
    pass
  # print_msg method
  def print_msg( self, msg ):
    print( "Calling start_requests in YourSpider prints out:", msg )
  
# Inspect Your Class
inspect_class( YourSpider )