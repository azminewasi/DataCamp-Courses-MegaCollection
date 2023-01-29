"""Comparing Dask & pandas execution times
The function you created in the last exercise can be used with either Dask or Pandas DataFrames. The only difference is that after the function is run on a Dask DataFrame, .compute() must be called on the result to perform the computation.

Your job is to run the by_region function separately on a Pandas DataFrame and a Dask DataFrame read from the same CSV file. To help understand how much time is taken when reading the file you'll compare the execution of the function with the Dask DataFrame to the Pandas DataFrame where the time taken to call pd.read_csv is included or ignored."""

"""Time the execution of pd.read_csv() and by_region together with 'WDI.csv' and print in milliseconds."""

# Call time.time()
t0 = time.time()

# Read 'WDI.csv' into df
df =pd.read_csv('WDI.csv')

# Group df by region: result
result = by_region(df)

# Call time.time()
t1 = time.time()

# Print the execution time
print((t1-t0)*1000)


"""    Now, time the execution of just by_region() with pandas and print in milliseconds."""

# Time the execution of just by_region with Pandas and print in milliseconds
df = pd.read_csv('WDI.csv')
t0 = time.time()
result = by_region(df)

t1 = time.time()
print((t1-t0)*1000)


"""
Now to see whether Dask is faster! Time the execution of dd.read_csv() and by_region together with 'WDI.csv' and print in milliseconds."""

# Time the execution of dd.read_csv and by_region together with 'WDI.csv' and print in milliseconds
t0 = time.time()
df = dd.read_csv('WDI.csv')
result =  by_region(df)
t1 = time.time()
print((t1-t0)*1000)