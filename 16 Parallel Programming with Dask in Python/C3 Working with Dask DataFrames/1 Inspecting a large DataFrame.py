"""Inspecting a large DataFrame
A Dask DataFrame is provided for you called df. This DataFrame connects to the World Development Indicators data set you worked with earlier.

Your job is to inspect this Dask DataFrame using methods and correctly identify the number of columns, the number of rows, and the number of unique countries from either the Country Name or Country Code columns. You can use methods you are already familiar with such as .describe() and .info(). Remember to also use .compute(), since df is a Dask (and not pandas) DataFrame.

Instructions
50 XP
Instructions
50 XP
Possible Answers

n_columns = 5; n_rows = 74458; n_countries = 36

n_columns = 7; n_rows = 123156; n_countries = 217

n_columns = 7; n_rows = 74458; n_countries = 36

n_columns = 5; n_rows = 123156; n_countries = 217"""