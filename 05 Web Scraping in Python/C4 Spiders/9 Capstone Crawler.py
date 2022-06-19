"""Capstone Crawler
This exercise gives you a chance to show off what you've learned! In this exercise, you will write the parse function for a spider and then fill in a few blanks to finish off the spider. On the course directory page of DataCamp, each listed course has a title and a short course description. This spider will be used to scrape the course directory to extract the course titles and short course descriptions. You will not need to follow any links this time. Everything you need to know is:

The course titles are defined by the text within an h4 element whose class contains the string block__title (double underline).
The short course descriptions are defined by the text within a paragraph p element whose class contains the string block__description (double underline).
"""

"""
Instructions
Assign to the variable crs_titles the extracted list of course titles on the DataCamp course directory page. You should use the contains call within your XPath, and your XPath string should point to the text of the selected objects.
Assign to the variable crs_descrs the extracted list of short course descriptions. You should use the contains call within your XPath. You should use the contains call within your XPath, and your XPath string should point to the text of the selected objects.
(Since we want a list of extracted data, we will use the extract() call (rather than extract_first()). )"""

# parse method
def parse(self, response):
  # Extracted course titles
  crs_titles = response.xpath('//h4[contains(@class,"block__title")]/text()').extract()
  # Extracted course descriptions
  crs_descrs = response.xpath('//p[contains(@class,"block__description")]/text()').extract()
  # Fill in the dictionary
  for crs_title, crs_descr in zip(crs_titles, crs_descrs):
    dc_dict[crs_title] = crs_descr


"""    Fill in the four blanks below with the necessary entries to complete your spider.
Note: If you hit Run Code, you will need to Reset to Sample before hitting Run Code again."""

# Import scrapy
import scrapy

# Import the CrawlerProcess
from scrapy.crawler import CrawlerProcess

# Create the Spider class
class YourSpider(scrapy.Spider):
  name = 'yourspider'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request(url = url_short, callback=self.parse)
      
  def parse(self, response):
    # My version of the parser you wrote in the previous part
    crs_titles = response.xpath('//h4[contains(@class,"block__title")]/text()').extract()
    crs_descrs = response.xpath('//p[contains(@class,"block__description")]/text()').extract()
    for crs_title, crs_descr in zip( crs_titles, crs_descrs ):
      dc_dict[crs_title] = crs_descr
    
# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(YourSpider)
process.start()

# Print a preview of courses
previewCourses(dc_dict)