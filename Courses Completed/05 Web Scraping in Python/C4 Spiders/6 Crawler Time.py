"""Crawler Time
This will be your first chance to play with a spider which will crawl between sites (by first collecting links from one site, and following those links to parse new sites). This spider starts at the shortened DataCamp course directory, then extracts the links of the courses in the parse method; from there, it will follow those links to extract the course descriptions from each course page in the parse_descr method, and put these descriptions into the list course_descrs. Your job is to complete the code so that the spider runs as desired!

We have created a function inspect_spider which will print out one of the course descriptions you scrape (if done correctly)!

Instructions
100 XP
Instructions
100 XP
Fill in the two blanks below (one in each of the parsing methods) with the appropriate entries so that the spider can move from the first parsing method to the second correctly."""
# Import the scrapy library
import scrapy

# Create the Spider class
class DCdescr( scrapy.Spider ):
  name = 'dcdescr'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = url_short, callback = self.parse )
  
  # First parse method
  def parse( self, response ):
    links = response.css( 'div.course-block > a::attr(href)' ).extract()
    # Follow each of the extracted links
    for link in links:
      yield response.follow( url = link, callback = self.parse_descr )
      
  # Second parsing method
  def parse_descr(self, response):
    # Extract course description
    course_descr = response.css( 'p.course__description::text' ).extract_first()
    # For now, just yield the course description
    yield course_descr


# Inspect the spider
inspect_spider( DCdescr )