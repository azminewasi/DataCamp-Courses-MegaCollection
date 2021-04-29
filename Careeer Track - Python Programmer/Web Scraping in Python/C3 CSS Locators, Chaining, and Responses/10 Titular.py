"""Titular
Similar to the work given in the previous lesson, we will have you use a pre-loaded Response object, named response to scrape the course titles from the (shortened version of the) DataCamp course directory https://www.datacamp.com/courses/all. To successfully do so, you only need to know the following

The course titles are the text from all the h4 elements within the HTML document.
We ask you to extract these course titles here.

Instructions
Using response, assign to the variable crs_title_els a SelectorList of the selected course titles.
Assign to the variable crs_titles a list created by extracting the course titles from crs_title_els."""

# Create a SelectorList of the course titles
crs_title_els = 'h4 ::text'

# Extract the course titles 
crs_titles = response.css(crs_title_els ).extract()

# Print out the course titles 
for el in crs_titles:
  print( ">>", el )