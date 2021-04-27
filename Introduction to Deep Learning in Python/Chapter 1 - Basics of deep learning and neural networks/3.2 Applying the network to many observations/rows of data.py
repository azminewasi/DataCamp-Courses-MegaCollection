'''
Applying the network to many observations/rows of data
You'll now define a function called predict_with_network() which will generate predictions for multiple data observations, which are pre-loaded as input_data. As before, weights are also pre-loaded. In addition, the relu() function you defined in the previous exercise has been pre-loaded.

Instructions
100 XP
Define a function called predict_with_network() that accepts two arguments - input_data_row and weights - and returns a prediction from the network as the output.
Calculate the input and output values for each node, storing them as: node_0_input, node_0_output, node_1_input, and node_1_output.
To calculate the input value of a node, multiply the relevant arrays together and compute their sum.
To calculate the output value of a node, apply the relu() function to the input value of the node.
Calculate the model output by calculating input_to_final_layer and model_output in the same way you calculated the input and output values for the nodes.
Use a for loop to iterate over input_data:
Use your predict_with_network() to generate predictions for each row of the input_data - input_data_row. Append each prediction to results.

'''