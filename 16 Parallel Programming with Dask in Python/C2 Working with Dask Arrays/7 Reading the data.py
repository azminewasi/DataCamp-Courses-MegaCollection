"""Reading the data
For this exercise, the monthly average maximum temperature (degrees Celsius) data on a 10km grid has been downloaded from NOAA for the continental US.

The data is stored in separate HDF5 files from 2008 to 2011. Your job is to use h5py to connect to the datasets and prepare a list of Dask arrays where each element is one year of data. The list of filenames is provided for you as filenames. The chunksizes have been chosen to optimize reading data from disk.

For this exercise you'll utilize a list comprehension to quickly iterate through the filenames list and form a new list of h5py file handles and again to make a list of Dask arrays.

Instructions
Import h5py, and dask.array as da.
Write a list comprehension to read each file with h5py.File() and select the /tmax key.
Write a list comprehension to read the h5py files into Dask arrays with chunks (1,444,922)."""

# Import h5py and dask.array
import h5py
import dask.array as da

# List comprehension to read each file: dsets
dsets = [h5py.File(f)["/tmax"] for f in filenames]

# List comprehension to make dask arrays: monthly
monthly = [da.from_array(d, chunks=(1,444,922)) for d in dsets]