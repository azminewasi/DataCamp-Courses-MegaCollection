"""Timing Dask array computations
Your job now is to create two Dask arrays from energy using different chunksizes. You'll then measure the time required (in milliseconds) to compute the standard deviation of each Dask array.

The NumPy array energy is provided as before and the module dask.array is imported for you as da.

Instructions
Import the time module.
Invoke da.from_array() using energy with chunks set to 1/4 the length of energy.
Print the time in milliseconds to compute standard deviation with a dask.array with 4 chunks.
"""

# Import time
import time

# Call da.from_array() with arr: energy_dask4
energy_dask4 = da.from_array(energy,chunks=energy.shape[0]//4)

# Print the time to compute standard deviation
t_start = time.time()
std_4 = energy_dask4.std().compute()
t_end = time.time()
print((t_end - t_start) * 1.0e3)


"""
Import the time module.
Invoke da.from_array() using energy with chunks set to 1/4 the length of energy.
Print the time in milliseconds to compute standard deviation with a dask.array with 4 chunks.
"""
# Import time
import time

# Call da.from_array() with arr: energy_dask8
energy_dask8 = da.from_array(energy,chunks=energy.shape[0]//8)

# Print the time to compute standard deviation
t_start = time.time()
std_8 = energy_dask8.std().compute()
t_end = time.time()
print((t_end - t_start) * 1.0e3)
