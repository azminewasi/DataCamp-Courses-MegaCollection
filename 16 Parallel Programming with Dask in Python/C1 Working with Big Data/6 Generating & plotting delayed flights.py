"""Generating & plotting delayed flights
Now that you have a function to compute flight delays, you'll apply it with a generator to analyze the percentage of delayed flights for each month of 2016.

You'll create a generator expression to loop over the provided list filenames and return a sequence of DataFrames. For each DataFrame, you'll then apply the function pct_delayed() (provided for you) within a list comprehension. Finally, you'll plot the results (matplotlib and pandas have been imported for you).

Warning: This exercise requires several seconds to execute.

Instructions
Construct a generator called dataframes that applies pd.read_csv() to all the elements of the list filenames.
Make a list comprehension called monthly_delayed in which the function pct_delayed() is applied to every element of dataframes.
Hit 'Submit Answer' to generate the plot.
"""

# Define the generator: dataframes
dataframes = (pd.read_csv(file) for file in filenames)

# Create the list comprehension: monthly_delayed
monthly_delayed = [pct_delayed(df) for df in dataframes]

# Create the plot
x = range(1,13)
plt.plot(x, monthly_delayed, marker='o', linewidth=0)
plt.ylabel('% Delayed')
plt.xlabel('Month - 2016')
plt.xlim((1,12))
plt.ylim((0,100))
plt.show()