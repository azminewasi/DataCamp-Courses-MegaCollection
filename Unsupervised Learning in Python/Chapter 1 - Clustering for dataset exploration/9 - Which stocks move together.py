'''
Which stocks move together?
In the previous exercise, you clustered companies by their daily stock price movements. So which company have stock prices that tend to change in the same way? You'll now inspect the cluster labels from your clustering to find out.

Your solution to the previous exercise has already been run. Recall that you constructed a Pipeline pipeline containing a KMeans model and fit it to the NumPy array movements of daily stock movements. In addition, a list companies of the company names is available.

Instructions
Import pandas as pd.
Use the .predict() method of the pipeline to predict the labels for movements.
Align the cluster labels with the list of company names companies by creating a DataFrame df with labels and companies as columns. This has been done for you.
Use the .sort_values() method of df to sort the DataFrame by the 'labels' column, and print the result.
Hit 'Submit Answer' and take a moment to see which companies are together in each cluster!
'''

# Import pandas
import pandas as pd

# Predict the cluster labels: labels
labels = pipeline.predict(movements)

# Create a DataFrame aligning labels and companies: df
df = pd.DataFrame({'labels': labels, 'companies': companies})

# Display df sorted by cluster label
print(df.sort_values('labels'))
