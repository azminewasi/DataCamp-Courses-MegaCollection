"""Stacking data & reading climatology
Now that we have a list of Dask arrays, your job is to call da.stack() to make a single Dask array where month and year are in separate dimensions. You'll also read the climatology data set, which is the monthly average max temperature again from 1970 to 2000."""

# Stack with the list of dask arrays: by_year
by_year = da.stack(monthly, axis=0)

# Print the shape of the stacked arrays
print(by_year.shape)

# Read the climatology data: climatology
dset = h5py.File('tmax.climate.hdf5')
climatology = da.from_array(dset['/tmax'], chunks=(1,444,922))

# Reshape the climatology data to be compatible with months
climatology.reshape((1,12,444,922))