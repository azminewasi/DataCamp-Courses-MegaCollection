'''
Clustering 2D points
From the scatter plot of the previous exercise, you saw that the points seem to separate into 3 clusters. You'll now create a KMeans model to find 3 clusters, and fit it to the data points from the previous exercise. After the model has been fit, you'll obtain the cluster labels for some new points using the .predict() method.

You are given the array points from the previous exercise, and also an array new_points.

Instructions 100 XP
Import KMeans from sklearn.cluster.
Using KMeans(), create a KMeans instance called model to find 3 clusters. To specify the number of clusters, use the n_clusters keyword argument.
Use the .fit() method of model to fit the model to the array of points points.
Use the .predict() method of model to predict the cluster labels of new_points, assigning the result to labels.
Hit 'Submit Answer' to see the cluster labels of new_points.
'''

# Import KMeans
from sklearn.cluster import KMeans 

# Create a KMeans instance with 3 clusters: model
model = KMeans (n_clusters=3)

# Fit model to points
model.fit(points)

# Determine the cluster labels of new_points: labels
labels = model.predict(new_points)

# Print cluster labels of new_points
print(labels)
