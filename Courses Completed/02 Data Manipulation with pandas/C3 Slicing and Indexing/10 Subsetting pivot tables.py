"""Subsetting pivot tables
A pivot table is just a DataFrame with sorted indexes, so the techniques you have learned already can be used to subset them. In particular, the .loc[] + slicing combination is often helpful.

pandas is loaded as pd. temp_by_country_city_vs_year is available.

Instructions
100 XP
Use .loc[] on temp_by_country_city_vs_year to take subsets.

From Egypt to India.
From Egypt, Cairo to India, Delhi.
From Egypt, Cairo to India, Delhi, and 2005 to 2010.

"""
# Subset for Egypt to India
temp_by_country_city_vs_year.loc["Egypt":"India"]

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India","Delhi")]

# Subset in both directions at once
temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India","Delhi"), '2005':'2010']
