'''
Hold-out set in practice II: Regression
Remember lasso and ridge regression from the previous chapter? Lasso used the  penalty to regularize, while ridge used the  penalty. There is another type of regularized regression known as the elastic net. In elastic net regularization, the penalty term is a linear combination of the  and  penalties:


In scikit-learn, this term is represented by the 'l1_ratio' parameter: An 'l1_ratio' of 1 corresponds to an  penalty, and anything lower is a combination of  and .

In this exercise, you will GridSearchCV to tune the 'l1_ratio' of an elastic net model trained on the Gapminder data. As in the previous exercise, use a hold-out set to evaluate your model's performance.

Instructions
100 XP
Instructions
100 XP
Import the following modules:
ElasticNet from sklearn.linear_model.
mean_squared_error from sklearn.metrics.
GridSearchCV and train_test_split from sklearn.model_selection.
Create training and test sets, with 40% of the data used for the test set. Use a random state of 42.
Specify the hyperparameter grid for 'l1_ratio' using l1_space as the grid of values to search over.
Instantiate the ElasticNet regressor.
Use GridSearchCV with 5-fold cross-validation to tune 'l1_ratio' on the training data X_train and y_train. This involves first instantiating the GridSearchCV object with the correct parameters and then fitting it to the training data.
Predict on the test set and compute the  and mean squared error.
'''

# Import necessary modules
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size =0.4,random_state =42)

# Create the hyperparameter grid
l1_space = np.linspace(0, 1, 30)
param_grid = {'l1_ratio':l1_space}

# Instantiate the ElasticNet regressor: elastic_net
elastic_net = ElasticNet()

# Setup the GridSearchCV object: gm_cv
gm_cv = GridSearchCV(elastic_net, param_grid, cv=5)

# Fit it to the training data

gm_cv.fit(X_train,y_train)
# Predict on the test set and compute metrics
y_pred = gm_cv.predict(X_test)
r2 = gm_cv.score(X_test, y_test)
mse = mean_squared_error(y_test, y_pred)
print("Tuned ElasticNet l1 ratio: {}".format(gm_cv.best_params_))
print("Tuned ElasticNet R squared: {}".format(r2))
print("Tuned ElasticNet MSE: {}".format(mse))
