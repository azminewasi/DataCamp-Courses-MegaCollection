'''
Setting up a train-test split in scikit-learn
Alright, you've been patient and awesome. It's finally time to start training models!

The first step is to split the data into a training set and a test set. Some labels don't occur very often, but we want to make sure that they appear in both the training and the test sets. We provide a function that will make sure at least min_count examples of each label appear in each split: multilabel_train_test_split.

Feel free to check out the full code for multilabel_train_test_split here.

You'll start with a simple model that uses just the numeric columns of your DataFrame when calling multilabel_train_test_split. The data has been read into a DataFrame df and a list consisting of just the numeric columns is available as NUMERIC_COLUMNS.

Instructions
Create a new DataFrame named numeric_data_only by applying the .fillna(-1000) method to the numeric columns (available in the list NUMERIC_COLUMNS) of df.
Convert the labels (available in the list LABELS) to dummy variables. Save the result as label_dummies.
In the call to multilabel_train_test_split(), set the size of your test set to be 0.2. Use a seed of 123.
Fill in the .info() method calls for X_train, X_test, y_train, and y_test.
'''
# Create the new DataFrame: numeric_data_only
numeric_data_only = df[NUMERIC_COLUMNS].fillna(-1000)

# Get labels and convert to dummy variables: label_dummies
label_dummies =  pd.get_dummies(df[LABELS])

# Create training and test sets
X_train, X_test, y_train, y_test = multilabel_train_test_split(numeric_data_only,label_dummies, size=0.2, seed=123)

# Print the info
print("X_train info:")
print(X_train.info())
print("\nX_test info:")  
print(X_test.info())
print("\ny_train info:")  
print(y_train.info())
print("\ny_test info:")  
print(y_test.info()) 