'''
Creating dummy variables
As Andy discussed in the video, scikit-learn does not accept non-numerical features. You saw in the previous exercise that the 'Region' feature contains very useful information that can predict life expectancy. For example, Sub-Saharan Africa has a lower life expectancy compared to Europe and Central Asia. Therefore, if you are trying to predict life expectancy, it would be preferable to retain the 'Region' feature. To do this, you need to binarize it by creating dummy variables, which is what you will do in this exercise.

Instructions

Use the pandas get_dummies() function to create dummy variables from the df DataFrame. Store the result as df_region.
Print the columns of df_region. This has been done for you.
Use the get_dummies() function again, this time specifying drop_first=True to drop the unneeded dummy variable (in this case, 'Region_America').
Hit 'Submit Answer to print the new columns of df_region and take note of how one column was dropped!
'''

# Create dummy variables: df_region
df_region = pd.get_dummies(df)

# Print the columns of df_region
print(df_region.columns)

# Create dummy variables with drop_first=True: df_region
df_region = df_region.drop('Region_America', axis=1)

# Print the new columns of df_region
print(df_region.columns)
