Understanding your classification data
Now you will start modeling with a new dataset for a classification problem. This data includes information about passengers on the Titanic. You will use predictors such as age, fare and where each passenger embarked from to predict who will survive. This data is from a tutorial on data science competitions. Look here for descriptions of the features.

The data is pre-loaded in a pandas DataFrame called df.

It's smart to review the maximum and minimum values of each variable to ensure the data isn't misformatted or corrupted. What was the maximum age of passengers on the Titanic? Use the .describe() method in the IPython Shell to answer this question.

Instructions
50 XP
Instructions
50 XP
Possible Answers

29.699.

80.

891.

It is not listed.

Submit Answer



=======================================================================================================================================================


In [1]:
df.describe()
Out[1]:

         survived      pclass         age       sibsp       parch        fare        male  embarked_from_cherbourg  embarked_from_queenstown  embarked_from_southampton
count  891.000000  891.000000  891.000000  891.000000  891.000000  891.000000  891.000000               891.000000                891.000000                 891.000000
mean     0.383838    2.308642   29.699118    0.523008    0.381594   32.204208    0.647587                 0.188552                  0.086420                   0.722783
std      0.486592    0.836071   13.002015    1.102743    0.806057   49.693429    0.477990                 0.391372                  0.281141                   0.447876
min      0.000000    1.000000    0.420000    0.000000    0.000000    0.000000    0.000000                 0.000000                  0.000000                   0.000000
25%      0.000000    2.000000   22.000000    0.000000    0.000000    7.910400    0.000000                 0.000000                  0.000000                   0.000000
50%      0.000000    3.000000   29.699118    0.000000    0.000000   14.454200    1.000000                 0.000000                  0.000000                   1.000000
75%      1.000000    3.000000   35.000000    1.000000    0.000000   31.000000    1.000000                 0.000000                  0.000000                   1.000000
max      1.000000    3.000000   80.000000    8.000000    6.000000  512.329200    1.000000                 1.000000                  1.000000                   1.000000