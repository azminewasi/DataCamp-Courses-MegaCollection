"""Chunking a NumPy array
A NumPy array has been provided for you as energy. This is the electricity load in kWh for the state of Texas sampled every 15 minutes over the year 2000 (that's about 35 thousand samples).

Your job is to convert the NumPy array into a dask.array; the dask.array should have chunks whose sizes are 1/4 of the number of elements of the array energy. You will then inspect the chunk sizes of the Dask array. Finally, you'll compute the mean electricity load in kWh in two ways (using the dask.array and using the NumPy array) to compare the results.

Instructions
Invoke da.from_array() with energy and chunks= 1/4 length of array energy.
Print energy_dask.chunks.
Print the mean value of the Dask array energy_dask, and then the mean value of the NumPy array energy."""

# Call da.from_array():  energy_dask
energy_dask = da.from_array(energy, chunks=energy.shape[0]//4)

# Print energy_dask.chunks
print(energy_dask.chunks)

# Print Dask array average and then NumPy array average
print(energy_dask.mean().compute())
print(energy.mean())