"""Pen Names
In this exercise, we have set up a spider class which, when finished, will retrieve the author names from a shortened version of the DataCamp course directory. The URL for the shortened version is stored in the variable url_short. Your job will be to create the list of extracted author names in the parse method of the spider.

Two things you should know:

You will be using the response object and the css method here.
The course author names are defined by the text within the paragraph p elements belonging to the class course-block__author-name
You can inspect the spider using the function inspect_spider() that we built for you -- it will print out the author names you find!

Note that this and the remaining exercises in this chapter may take some time to load.

Instructions
100 XP
Instructions
100 XP
Fill in the required arguments to the parse method so that it will work as required when called in the start_requests method.
Within the parse method, create a variable author_names, which is a list of strings created by extracting the text from the paragraph elements belonging to the class course-block__author-name.

"""













# Import the scrapy library
import scrapy

# Create the Spider class
class DCspider( scrapy.Spider ):
  name = 'dcspider'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = url_short, callback = self.parse )
  # parse method
  def parse( self, response ):
    # Create an extracted list of course author names
    author_names=response.css('p.course-block__author-name ::text').extract()
    # Here we will just return the list of Authors
    return author_names
  
# Inspect the spider
inspect_spider( DCspider )