Subsetting rows by categorical variables
Subsetting data based on a categorical variable often involves using the "or" operator (|) to select rows from multiple categories. This can get tedious when you want all states in one of three different regions, for example. Instead, use the .isin() method, which will allow you to tackle this problem by writing one condition instead of three separate ones.

colors = ["brown", "black", "tan"]
condition = dogs["color"].isin(colors)
dogs[condition]
homelessness is available and pandas is loaded as pd.

Instructions 2/2
0 XP
Instructions 2/2
0 XP
Filter homelessness for cases where the USA census region is "South Atlantic" or it is "Mid-Atlantic", assigning to south_mid_atlantic. View the printed result.

Filter homelessness for cases where the USA census state is in the list of Mojave states, canu, assigning to mojave_homelessness. View the printed result.


Hint
The solution takes the form df[df["col"].isin(["value_1", "value_2"])].



# Select the individuals column
individuals = homelessness['individuals']

# Print the head of the result
print(individuals.head())