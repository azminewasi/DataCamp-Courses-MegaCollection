'''
Instantiate pipeline
In order to make your life easier as you start to work with all of the data in your original DataFrame, df, it's time to turn to one of scikit-learn's most useful objects: the Pipeline.

For the next few exercises, you'll reacquaint yourself with pipelines and train a classifier on some synthetic (sample) data of multiple datatypes before using the same techniques on the main dataset.

The sample data is stored in the DataFrame, sample_df, which has three kinds of feature data: numeric, text, and numeric with missing values. It also has a label column with two classes, a and b.

In this exercise, your job is to instantiate a pipeline that trains using the numeric column of the sample data.

Instructions
100 XP
Instructions
100 XP
Import Pipeline from sklearn.pipeline.
Create training and test sets using the numeric data only. Do this by specifying sample_df[['numeric']] in train_test_split().
Instantiate a pipeline as pl by adding the classifier step. Use a name of 'clf' and the same classifier from Chapter 2: OneVsRestClassifier(LogisticRegression()).
Fit your pipeline to the training data and compute its accuracy to see it in action! Since this is toy data, you'll use the default scoring method for now. In the next chapter, you'll return to log loss scoring.
'''

# Import Pipeline
from sklearn.pipeline import Pipeline

# Import other necessary modules
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

# Split and select numeric data only, no nans 
X_train, X_test, y_train, y_test = train_test_split(sample_df[['numeric']],
                                                    pd.get_dummies(sample_df['label']), 
                                                    random_state=22)

# Instantiate Pipeline object: pl

pl = Pipeline([
        ('clf',OneVsRestClassifier(LogisticRegression()) )
    ])

# Fit the pipeline to the training data
pl.fit(X_train,y_train)

# Compute and print accuracy
accuracy = pl.score(X_test,y_test)
print("\nAccuracy on sample data - numeric, no nans: ", accuracy)