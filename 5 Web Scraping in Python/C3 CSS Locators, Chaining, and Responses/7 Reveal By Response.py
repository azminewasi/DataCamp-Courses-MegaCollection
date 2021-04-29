"""Reveal By Response
We have pre-loaded a Response object, named response, with the content from a secret website. Your job is to figure out the URL and the title of the website using the response variable. You learned how to find the URL in the last lesson. To find the website title, what you need to know is:

The title is the text from the title element
The title element is a child of the head element, which is a child of the html root element.
To note: the html root element only has one child head element, and the head element only has one child title element.

Instructions
Assign to the variable this_url the URL used to load the response variable.
Assign to the variable this_title the title of the website used to load the response variable. Since we only want the text from the single element we will select, we use the extract_first() method to extract the text.
Regardless of whether you use xpath or css, make sure that you are selecting the text within the title element, and not just the title itself."""

# Get the URL to the website loaded in response
this_url =response.url

# Get the title of the website loaded in response
this_title = response.css('title::text').extract_first()

# Print out our findings
print_url_title( this_url, this_title )