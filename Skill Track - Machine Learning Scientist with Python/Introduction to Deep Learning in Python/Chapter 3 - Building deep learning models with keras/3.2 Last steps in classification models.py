Last steps in classification models
You'll now create a classification model using the titanic dataset, which has been pre-loaded into a DataFrame called df. You'll take information about the passengers and predict which ones survived.

The predictive variables are stored in a NumPy array predictors. The target to predict is in df.survived, though you'll have to manipulate it for keras. The number of predictive features is stored in n_cols.

Here, you'll use the 'sgd' optimizer, which stands for Stochastic Gradient Descent. You'll learn more about this in the next chapter!

Instructions
100 XP
Instructions
100 XP
Convert df.survived to a categorical variable using the to_categorical() function.
Specify a Sequential model called model.
Add a Dense layer with 32 nodes. Use 'relu' as the activation and (n_cols,) as the input_shape.
Add the Dense output layer. Because there are two outcomes, it should have 2 units, and because it is a classification model, the activation should be 'softmax'.
Compile the model, using 'sgd' as the optimizer, 'categorical_crossentropy' as the loss function, and metrics=['accuracy'] to see the accuracy (what fraction of predictions were correct) at the end of each epoch.
Fit the model using the predictors and the target.

==================================================================================================================


# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical

# Convert the target to categorical: target
target = to_categorical(df.survived)

# Set up the model
model = Sequential()

# Add the first layer
model.add(Dense(32, activation='relu', input_shape=(n_cols,)))

# Add the output layer
model.add(Dense(2,activation='softmax'))

# Compile the model
model.compile(optimizer='sgd', loss='categorical_crossentropy',metrics=['accuracy'])

# Fit the model
model.fit(predictors,target)

==================================================================================================================

<script.py> output:
    Epoch 1/10
    
 32/891 [>.............................] - ETA: 2s - loss: 7.6250 - acc: 0.2188
768/891 [========================>.....] - ETA: 0s - loss: 2.3826 - acc: 0.6042
891/891 [==============================] - 0s - loss: 2.5170 - acc: 0.5948     
    Epoch 2/10
    
 32/891 [>.............................] - ETA: 0s - loss: 1.1922 - acc: 0.3125
576/891 [==================>...........] - ETA: 0s - loss: 1.3212 - acc: 0.5729
891/891 [==============================] - 0s - loss: 1.1838 - acc: 0.6083     
    Epoch 3/10
    
 32/891 [>.............................] - ETA: 0s - loss: 2.1593 - acc: 0.5000
608/891 [===================>..........] - ETA: 0s - loss: 0.8669 - acc: 0.6398
891/891 [==============================] - 0s - loss: 0.7866 - acc: 0.6689     
    Epoch 4/10
    
 32/891 [>.............................] - ETA: 0s - loss: 0.7265 - acc: 0.5625
608/891 [===================>..........] - ETA: 0s - loss: 0.6632 - acc: 0.6661
891/891 [==============================] - 0s - loss: 0.7281 - acc: 0.6678     
    Epoch 5/10
    
 32/891 [>.............................] - ETA: 0s - loss: 0.6178 - acc: 0.5938
832/891 [===========================>..] - ETA: 0s - loss: 0.6488 - acc: 0.6526
891/891 [==============================] - 0s - loss: 0.6553 - acc: 0.6566     
    Epoch 6/10
    
 32/891 [>.............................] - ETA: 0s - loss: 0.4732 - acc: 0.7500
800/891 [=========================>....] - ETA: 0s - loss: 0.6193 - acc: 0.6900
891/891 [==============================] - 0s - loss: 0.6165 - acc: 0.6914     
    Epoch 7/10
    
 32/891 [>.............................] - ETA: 0s - loss: 0.6638 - acc: 0.5938
832/891 [===========================>..] - ETA: 0s - loss: 0.6396 - acc: 0.6827
891/891 [==============================] - 0s - loss: 0.6361 - acc: 0.6846     
    Epoch 8/10
    
 32/891 [>.............................] - ETA: 0s - loss: 0.5088 - acc: 0.7500
832/891 [===========================>..] - ETA: 0s - loss: 0.6258 - acc: 0.6863
891/891 [==============================] - 0s - loss: 0.6295 - acc: 0.6857     
    Epoch 9/10
    
 32/891 [>.............................] - ETA: 0s - loss: 0.6712 - acc: 0.6250
832/891 [===========================>..] - ETA: 0s - loss: 0.6058 - acc: 0.6923
891/891 [==============================] - 0s - loss: 0.5966 - acc: 0.6970     
    Epoch 10/10
    
 32/891 [>.............................] - ETA: 0s - loss: 0.4733 - acc: 0.7500
832/891 [===========================>..] - ETA: 0s - loss: 0.6340 - acc: 0.6839
891/891 [==============================] - 0s - loss: 0.6366 - acc: 0.6801     
In [1]:

