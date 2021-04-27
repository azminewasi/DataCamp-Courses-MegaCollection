'''
Try a different class of model
Now you're cruising. One of the great strengths of pipelines is how easy they make the process of testing different models.

Until now, you've been using the model step ('clf', OneVsRestClassifier(LogisticRegression())) in your pipeline.

But what if you want to try a different model? Do you need to build an entirely new pipeline? New nests? New FeatureUnions? Nope! You just have a simple one-line change, as you'll see in this exercise.

In particular, you'll swap out the logistic-regression model and replace it with a random forest classifier, which uses the statistics of an ensemble of decision trees to generate predictions.

Instructions

Import the RandomForestClassifier from sklearn.ensemble.
Add a RandomForestClassifier() step named 'clf' to the pipeline.
Hit 'Submit Answer' to fit the pipeline to the training data and compute its accuracy.
'''