"""Computing the average bill's lifespan
Some congressional bills can take years to get through committees, floor reading, voting and presidential signatures.

Each bill in the bills_dicts Dask Bag has 'current_status_date' and 'introduced_date' keys. Your job is to write a function that returns the number of days that have passed between these two dates. You'll then apply this function over the bills where the 'current_status' is 'enacted_signed'. Finally, you'll compute the average number of days. Pandas has been imported for you as pd and the bills_dicts Dask Bag has been provided.

Instructions
Define a function lifespan that takes a dictionary d as input.
Convert the 'current_status_date' and 'introduced_date' values of d to datetime with pd.to_datetime().
Take the difference between the current and intro objects and return the .days attribute
Print the mean value of the days Bag which has been filtered for you.
"""

# Define a function lifespan that takes a dictionary d as input
def lifespan(d):
    # Convert to datetime
    current = pd.to_datetime(d['current_status_date'])
    intro = pd.to_datetime(d['introduced_date'])

    # Return the number of days
    return (current - intro).days

# Filter bills_dicts: days
days = bills_dicts.filter(lambda s:s['current_status']=='enacted_signed').map(lifespan)

# Print the mean value of the days Bag
print(days.mean().compute())