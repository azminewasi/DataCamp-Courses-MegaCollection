"""Transforming, aggregating, and plotting
Now that we have two Dask arrays, one for the monthly average temperature from 2008 to 2011 and one for the 30-year climatology average we can compute the deviation from the climatology by taking a difference. The climatology data will be broadcast into each each year of the outer dimension of by_year.

Your job is to compute the difference, convert it to Fahrenheit, and take the average over the latitude and longitude dimensions. For this you'll use the da.nanmean() function, which ignores missing values. Finally, you'll make a plot of the monthly average deviation each year for January, August, and December.

The arrays you made in the last exercise are provided for you and the pyplot module from matplotlib has been imported as plt.

Instructions
Compute the difference between by_year and climatology and multiply by 9/5.
Using da.nanmean(), compute the average of the difference over the last two axes and call .compute(). You can use axis=(-1,-2) for the last two axes. Remember to also pass in diff as the first argument to da.nanmean().

"""

# Compute the difference: diff
diff = (by_year-climatology)*9/5
# Compute the average over last two axes: avg
avg = da.nanmean(diff,axis=(-1,-2)).compute()
# Plot the slices [:,0], [:,7], and [:11] against the x values
x = range(2008,2012)
f, ax = plt.subplots()
ax.plot(x,avg[:,0], label='Jan')
ax.plot(x,avg[:,7], label='Aug')
ax.plot(x,avg[:,11], label='Dec')
ax.axhline(0, color='red')
ax.set_xlabel('Year')
ax.set_ylabel('Difference (degrees Fahrenheit)')
ax.legend(loc=0)
plt.show()