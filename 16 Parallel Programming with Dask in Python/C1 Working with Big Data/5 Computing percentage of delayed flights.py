"""Computing percentage of delayed flights
Multiple CSV files of flight information have been provided from the Bureau of Transportation Statistics. Each file contains one month of information in 2016.

Your first job is to build a function to compute the percentage of delayed flights given a DataFrame of flight information. Your function will take a single DataFrame as input and compute the percentage of its rows in which the 'DEP_DELAY' value is greater than zero.

Instructions
Define a function called pct_delayed() function with a single input parameter df.
Compute the total number of delayed flights in df. If the 'DEP_DELAY' column is greater than 0, the flight is delayed. Use the .sum() method to compute the total number of delayed flights.
Return the percentage of delayed flights, i.e., n_delayed multiplied by 100 divided by len(df)."""


# Define function with single input called df: pct_delayed
def pct_delayed(df):
    # Compute number of delayed flights: n_delayed
    n_delayed = (df.DEP_DELAY>0).sum()
    # Return percentage of delayed flights
    return n_delayed  * 100 / len(df)