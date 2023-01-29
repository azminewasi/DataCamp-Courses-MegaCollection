"""Filtering vetoed bills
Now that you've got a Dask Bag prepared with congressional bills as dictionaries we can use filtering and mapping tools to find all of the bills since the 93rd congress that were vetoed by the sitting President and later overridden by congress.

The bills_dicts Dask Bag from the previous exercise is provided for you. Your job is to filter the bills to retain those where the current_status key is 'enacted_veto_override'. You'll then print the titles of the bills using .pluck. To help you do this, the following function has been defined for you:

# Compare the value of the 'current_status' key to 'enacted_veto_override'
def veto_override(d):
    return d['current_status'] == 'enacted_veto_override'


Instructions
Filter bills_dicts using the veto_override function.
Print the number of bills retained using .count() and .compute().
Use .pluck() to get the value of the 'title' key for each bill and assign to titles.
Compute the print the titles."""

# Filter the bills: overridden
overridden = bills_dicts.filter(veto_override)

# Print the number of bills retained
print(overridden.count().compute())

# Get the value of the 'title' key
titles = overridden.pluck('title')

# Compute and print the titles
print(titles.compute())