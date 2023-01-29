"""Reading & counting
The sotu/ directory contains text files for each of the 45 US Presidents as of 2017. These text files contain the State of the Union addresses delivered by each president. The texts of the speeches were obtained from the American Presidency Project.

The entire speech for each State of the Union address is on a single line in each text file; that is, individual addresses are separated by '\n'. For example, the 33rd US president Truman delivered 9 State of the Union speeches, so the file sotu/33Truman.txt has 9 lines). Distinct files, then have distinct numbers of lines according to the number of State of the Union addresses each president delivered during their presidency.

Instructions
Use glob.glob() to get a list of filenames matching the glob pattern 'sotu/*.txt' and then sort them using sorted().
Use the sorted filenames to create a Dask bag with db.read_text().
Print the number of speeches in the Dask bag with .count() and .compute()."""

# Glob filenames matching 'sotu/*.txt' and sort
filenames = glob.glob('sotu/*.txt')
filenames = sorted(filenames)

# Load filenames as Dask bag with db.read_text(): speeches
speeches = db.read_text(filenames)

# Print number of speeches with .count()
print(speeches.count().compute())