"""Which city gets the most snow?
The Dask DataFrame weather from the previous exercise is provided here.

Your task now is to aggregate the total snow fall for each airport (at least those airports that experienced snow). You'll use the method .str.contains() to create a boolean Series identifying snowy days. You'll need to chain with the method fillna(False) as well; this is to clean NaN values from the boolean Series so it can be used for selection within the .loc[] accessor. After filtering rows that correspond to snowy days from weather, you'll group the rows of the filtered DataFrame by airport code. This allows you to extract the precipitation column and compute aggregated sums grouped by airport."""
"""
Create a boolean array is_snowy from the 'Events' column of weather. Apply the method .str.contains() to find rows containing 'Snow' and chain a call to fillna(False) to replace NaN values with False.
Create a filtered DataFrame using is_snowy. Assign the result to got_snow.
Using got_snow, groupby the 'Airport' column, select the 'PrecipitationIn' column, and aggregate with sum(). Assign the final value as result.

"""

# Make cleaned Boolean Series from weather['Events']: is_snowy
is_snowy = weather['Events'].str.contains('Snow').fillna(False)

# Create filtered DataFrame with weather.loc & is_snowy: got_snow
got_snow = weather.loc[is_snowy]

# Groupby 'Airport' column; select 'PrecipitationIn'; aggregate sum(): result
result = got_snow.groupby('Airport')['PrecipitationIn'].sum()

# Compute & print the value of result
print(result.compute())