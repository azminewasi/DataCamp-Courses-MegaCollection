""""Subtracting & broadcasting
Now that you're comfortable with broadcasting rules, you're going to practice using the .reshape() method together with broadcasting.

The one-dimensional array load_2001 holds the total electricity load for the state of Texas sampled every 15 minutes for the entire year 2001 (35040 samples in total). The one-dimensional array load_recent holds the corresponding data sampled for each of the years 2013 through 2015 (i.e., 105120 samples consisting of the samples from 2013, 2014, & 2015 in sequence). None of these years are leap years, so each year has 365 days. Observe also that there are 96 intervals of duration 15 minutes in each day.

Your job is to compute the differences of the samples in the years 2013 to 2015 each from the corresponding samples of 2001.""""

# Reshape load_recent to three dimensions: load_recent_3d
load_recent_3d=load_recent.reshape((3,365,96))

# Reshape load_2001 to three dimensions: load_2001_3d
load_2001_3d = load_2001.reshape((1,365,96))

# Subtract the load in 2001 from the load in 2013 - 2015: diff_3d
diff_3d = load_recent_3d - load_2001_3d

# Print the difference each year on March 2 at noon
print(diff_3d[:,61, 48])