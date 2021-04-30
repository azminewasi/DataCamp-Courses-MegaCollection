"""Grouping & aggregating by year
The filtered Dask DataFrame from the previous exercise has been provided for you as filtered. In this exercise you're going to plot the average percent of the population exposed to air pollution in the East Asia & Pacific region from 2010 to 2015.

Your job is to use .groupby() to collect all of the individual country values by the 'Year' column and aggregate with the mean() function. You'll then call .compute() to perform the computation in parallel, and finally plot the results.

Instructions
Make a groupby object with .groupby() from filtered with 'Year' as input.
Aggregate the mean of the groupby object assigned to yearly_mean.
Call .compute() to perform the computation and assign to result.
Hit 'Submit Answer' to view the plot."""
# Grouby filtered by the 'Year' column: 
yearly=filtered.groupby('Year')


# Calculate the mean of yearly: 
yearly_mean=yearly.mean()


# Call .compute() to perform the computation: 
result=yearly_mean.compute()


# Plot the 'value' column with .plot.line()
result['value'].plot.line()
plt.ylabel('% pop exposed')
plt.show()