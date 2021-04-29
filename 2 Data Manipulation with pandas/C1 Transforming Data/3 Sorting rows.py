Sorting rows
Finding interesting bits of data in a DataFrame is often easier if you change the order of the rows. You can sort the rows by passing a column name to .sort_values().

In cases where rows have the same value (this is common if you sort on a categorical variable), you may wish to break the ties by sorting on another column. You can sort on multiple columns in this way by passing a list of column names.

Sort on …	Syntax
one column	df.sort_values("breed")
multiple columns	df.sort_values(["breed", "weight_kg"])
By combining .sort_values() with .head(), you can answer questions in the form, "What are the top cases where…?".

homelessness is available and pandas is loaded as pd.

Instructions 1/3

1
Sort homelessness by the number of homeless individuals, from smallest to largest, and save this as homelessness_ind.
Print the head of the sorted DataFrame.

Take Hint (-10 XP)
2
Sort homelessness by the number of homeless family_members in descending order, and save this as homelessness_fam.
Print the head of the sorted DataFrame.
3
Sort homelessness first by region (ascending), and then by number of family members (descending). Save this as homelessness_reg_fam.
Print the head of the sorted DataFrame.

==================================================================================================================
# Sort homelessness by individual
homelessness_ind = homelessness.sort_values("individuals")

# Print the top few rows
print(homelessness_ind.head())


# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values("family_members",ascending=False)

# Print the top few rows
print(homelessness_fam.head())




# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending=[True, False])


# Print the top few rows
print(homelessness_reg_fam.head())
