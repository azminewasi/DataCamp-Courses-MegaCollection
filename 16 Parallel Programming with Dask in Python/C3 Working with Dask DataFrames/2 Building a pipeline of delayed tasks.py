"""Building a pipeline of delayed tasks
For this exercise, you'll use a Dask DataFrame to read and process the World Bank's World Development Indicators.

Your job is to filter the DataFrame for the 'East Asia & Pacific' region and measurements of the percent population exposed to toxic air pollution. The output of this effort is a delayed Dask DataFrame; you'll compute the result in the next exercise.

The CSV file 'WDI.csv' has been truncated to reduce execution time.

Instructions
Read 'WDI.csv' with dd.read_csv() into a DataFrame called df.
Filter df using the Boolean arrays toxins and region."""

# Read from 'WDI.csv': df
df=dd.read_csv('WDI.csv')

# Boolean series where 'Indicator Code' is 'EN.ATM.PM25.MC.ZS': toxins
toxins = df['Indicator Code'] == 'EN.ATM.PM25.MC.ZS'
# Boolean series where 'Region' is 'East Asia & Pacific': region
region = df['Region'] == 'East Asia & Pacific'

# Filter the DataFrame using toxins & region: 
filtered=df.loc[toxins & region]
