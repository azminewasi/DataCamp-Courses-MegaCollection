'''
Multiple types of processing: FunctionTransformer
The next two exercises will introduce new topics you'll need to make your pipeline truly excel.

Any step in the pipeline must be an object that implements the fit and transform methods. The FunctionTransformer creates an object with these methods out of any Python function that you pass to it. We'll use it to help select subsets of data in a way that plays nicely with pipelines.

You are working with numeric data that needs imputation, and text data that needs to be converted into a bag-of-words. You'll create functions that separate the text from the numeric variables and see how the .fit() and .transform() methods work.

Instructions

Compute the selector get_text_data by using a lambda function and FunctionTransformer() to obtain all 'text' columns.
Compute the selector get_numeric_data by using a lambda function and FunctionTransformer() to obtain all the numeric columns (including missing data). These are 'numeric' and 'with_missing'.
Fit and transform get_text_data using the .fit_transform() method with sample_df as the argument.
Fit and transform get_numeric_data using the same approach as above.

'''
# Import FunctionTransformer
from sklearn.preprocessing import FunctionTransformer

# Obtain the text data: get_text_data
get_text_data = FunctionTransformer(lambda x: x['text'], validate=False)

# Obtain the numeric data: get_numeric_data
get_numeric_data = FunctionTransformer(lambda x: x[['numeric', 'with_missing']], validate=False)

# Fit and transform the text data: just_text_data
just_text_data = get_text_data.fit_transform(sample_df)

# Fit and transform the numeric data: just_numeric_data
just_numeric_data = get_numeric_data.fit_transform(sample_df)

# Print head to check results
print('Text Data')
print(just_text_data.head())
print('\nNumeric Data')
print(just_numeric_data.head())