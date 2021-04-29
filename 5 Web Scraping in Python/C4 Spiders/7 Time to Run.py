"""Time to Run
In the last lesson, we went through creating an entire web-crawler to access course information from each course in the DataCamp course directory. However, the lesson seemed to stop without a climax, because we didn't play with the code after finishing the parsing methods.

The point of this exercise is to remedy that!

The code we give you to look at in this and the next exercise is long, because its the entire spider that took us the lesson to create! However, don't be intimidated! The point of these two exercises is to give you a very easy task to complete, with the hope that you will look at and run the code for this spider. That way, even though it is long, you will have a grasp of it!

Instructions
100 XP
Fill in the one blank at the end of the parse_pages methods to assign the chapter titles to the dictionary whose key is the corresponding course title.
NOTE: If you hit Run Code, you must Reset to Sample Code to successfully use Run Code again!!"""

# Import scrapy
import scrapy

# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess

# Create the Spider class
class DC_Chapter_Spider(scrapy.Spider):
  name = "dc_chapter_spider"
  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url = url_short,
                         callback = self.parse_front)
  # First parsing method
  def parse_front(self, response):
    course_blocks = response.css('div.course-block')
    course_links = course_blocks.xpath('./a/@href')
    links_to_follow = course_links.extract()
    for url in links_to_follow:
      yield response.follow(url = url,
                            callback = self.parse_pages)
  # Second parsing method
  def parse_pages(self, response):
    crs_title = response.xpath('//h1[contains(@class,"title")]/text()')
    crs_title_ext = crs_title.extract_first().strip()
    ch_titles = response.css('h4.chapter__title::text')
    ch_titles_ext = [t.strip() for t in ch_titles.extract()]
    dc_dict[ crs_title_ext ] = ch_titles_ext

# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(DC_Chapter_Spider)
process.start()

# Print a preview of courses
previewCourses(dc_dict)