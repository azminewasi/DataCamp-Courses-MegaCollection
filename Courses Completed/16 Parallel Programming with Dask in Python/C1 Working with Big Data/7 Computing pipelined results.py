"""Computing pipelined results
Now that the dask.delayed functions are defined, we can use them to construct the pipeline of delayed tasks.

Your job is to loop over the file names, store the temporary information in lists, and aggregate the final result. Two empty lists, n_delayed, and n_flights, have been created for you.

The distinction here is that we are working with dask.delayed functions and objects, not real, computed values. The computation will only be executed when you call .compute() on the final result (by contrast with earlier exercises).

Warning: The expected execution time of this exercise is several seconds.

Instructions
Loop over the provided filenames list and call read_one() on file. This is the same read_one() you saw in the previous exercise.
Within the loop call, apply count_delayed to df and append the result to n_delayed. Do the same with count_flights and n_flights.
After the loop, call pct_delayed() with n_delayed and n_flights and assign the output to result.
Print the output of result.compute()."""

# Loop over the provided filenames list and call read_one: df
for file in filenames:
    df = read_one(file)

    # Append to n_delayed and n_flights
    n_delayed.append(count_delayed(df))
    n_flights.append(count_flights(df))

# Call pct_delayed with n_delayed and n_flights: result
result = pct_delayed(n_delayed,n_flights)

# Print the output of result.compute()
print(result.compute())