'''
Scaling fish data for clustering
You are given an array samples giving measurements of fish. Each row represents an individual fish. The measurements, such as weight in grams, length in centimeters, and the percentage ratio of height to length, have very different scales. In order to cluster this data effectively, you'll need to standardize these features first. In this exercise, you'll build a pipeline to standardize and cluster the data.

These fish measurement data were sourced from the Journal of Statistics Education.

Instructions
100 XP

Import:
make_pipeline from sklearn.pipeline.
StandardScaler from sklearn.preprocessing.
KMeans from sklearn.cluster.
Create an instance of StandardScaler called scaler.
Create an instance of KMeans with 4 clusters called kmeans.
Create a pipeline called pipeline that chains scaler and kmeans. To do this, you just need to pass them in as arguments to make_pipeline().

'''

# Perform the necessary imports
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Create scaler: scaler
scaler = StandardScaler()

# Create KMeans instance: kmeans
kmeans = KMeans (n_clusters=4)

# Create pipeline: pipeline
pipeline = make_pipeline(scaler,kmeans)
