"""Time to join!
While normalizing your text, you noticed that one review had a particular structure. This review ends with the HTML tag <\i> and it has a lot of commas in different places of the sentence. You decide to remove the tag from the end and use the strategy of splitting the string and joining it back again without the commas.

The text of a movie review has been already saved in the variable movie. You can use print(movie) to view the variable in the IPython Shell."""
# Remove tags happening at the end and print results
movie_tag = movie.rstrip("<\i>")
print(movie_tag)

# Split the string using commas and print results
movie_no_comma = movie_tag.split(",")
print(movie_no_comma)

# Join back together and print results
movie_join = " ".join(movie_no_comma)
print(movie_join)