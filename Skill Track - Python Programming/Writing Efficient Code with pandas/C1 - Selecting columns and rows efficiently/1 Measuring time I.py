Measuring time I
In the lecture slides, you saw how the time.time() function can be loaded and used to assess the time required to perform a basic mathematical operation.

Now, you will use the same strategy to assess two different methods for solving a similar problem: calculate the sum of squares of all the positive integers from 1 to 1 million (1,000,000).

Similar to what you saw in the video, you will compare two methods; one that uses brute force and one more mathematically sophisticated.

In the function formula, we use the standard formula

 
where N=1,000,000.

In the function brute_force we loop over each number from 1 to 1 million and add it to the result.

Instructions
Calculate the result of the problem using the formula() function.
Print the time required to calculate the result using the formula() function.
Calculate the result of the problem using the brute_force() function.
Print the time required to calculate the result using the brute_force() function.

==================================================================================================================

# Calculate the result of the problem using formula() and print the time required
N = 1000000
fm_start_time = time.time()
first_method = formula(N)
print("Time using formula: {} sec".format(time.time() - fm_start_time))

# Calculate the result of the problem using brute_force() and print the time required
sm_start_time = time.time()
second_method =brute_force(N)
print("Time using the brute force: {} sec".format(time.time() - sm_start_time))