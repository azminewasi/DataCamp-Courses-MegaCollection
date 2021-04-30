"""Filtering WDI data in chunks
Using the World Bank's World Development Indicators (or WDI) dataset, you're going to plot the percentage of the population of Australia in urban centers since 1980.

Your job is to loop over chunks of the WDI dataset; from each chunk, you will filter out rows describing Australia's "percent urban population." You'll then concatenate the filtered chunks and plot the results. pandas has been pre-imported for you as pd.

Instructions
Loop over the output of pd.read_csv() with 'WDI.csv' and chunksize=1000.
The filtered chunks is_urban and is_AUS have been created for you. Use .loc[] to filter from chunk using is_urban & is_AUS and assign to filtered.
Append the filtered chunk to the list dfs."""

# Create empty list: dfs
dfs = []

# Loop over 'WDI.csv'
for chunk in pd.read_csv('WDI.csv', chunksize=1000):
    # Create the first Series
    is_urban = chunk['Indicator Name']=='Urban population (% of total)'
    # Create the second Series
    is_AUS = chunk['Country Code']=='AUS'

    # Create the filtered chunk: filtered
    filtered=chunk.loc[is_urban & is_AUS]
    # Append the filtered chunk to the list dfs
    dfs.append(filtered)
