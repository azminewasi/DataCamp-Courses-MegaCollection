"""Preparing the pipeline
Since pandas and Dask share the same API, we can write functions that work for both libraries. Your job here is to write a function that takes a DataFrame as input, performs Boolean filtering, groupby, and returns the result.

In the next exercise you'll apply this function on Dask and pandas DataFrames and compare the time it takes to complete.

Instructions
Define the function by_region that takes a DataFrame df as input
Filter df using the two arrays toxins and y2015 and group by the 'Region' column.
Return the output of the mean() of the 'value' column from the regions groupby object.
"""

# Define a function with df as input: by_region
def by_region(df):

    # Create the toxins array
    toxins = df['Indicator Code'] == 'EN.ATM.PM25.MC.ZS'

    # Create the y2015 array
    y2015 = df['Year'] == 2015

    # Filter the DataFrame and group by the 'Region' column
    regions = df.loc[toxins & y2015].groupby('Region')

    # Return the mean of the 'value' column of regions
    return regions['value'].mean()
