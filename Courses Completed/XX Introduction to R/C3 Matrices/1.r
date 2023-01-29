# What's a matrix?
# In R, a matrix is a collection of elements of the same data type (numeric, character, or logical) arranged into a fixed number of rows and columns. Since you are only working with rows and columns, a matrix is called two-dimensional.
# 
# You can construct a matrix in R with the matrix() function. Consider the following example:
# 
# matrix(1:9, byrow = TRUE, nrow = 3)
# In the matrix() function:
# 
# The first argument is the collection of elements that R will arrange into the rows and columns of the matrix. Here, we use 1:9 which is a shortcut for c(1, 2, 3, 4, 5, 6, 7, 8, 9).
# The argument byrow indicates that the matrix is filled by the rows. If we want the matrix to be filled by the columns, we just place byrow = FALSE.
# The third argument nrow indicates that the matrix should have three rows.
# Instructions
# 100 XP
# Construct a matrix with 3 rows containing the numbers 1 up to 9, filled row-wise.

# Construct a matrix with 3 rows that contain the numbers 1 up to 9
matrix(1:9, byrow = TRUE, nrow = 3)

# 
# 
# 
# Analyze matrices, you shall
# It is now time to get your hands dirty. In the following exercises you will analyze the box office numbers of the Star Wars franchise. May the force be with you!
#   
#   In the editor, three vectors are defined. Each one represents the box office numbers from the first three Star Wars movies. The first element of each vector indicates the US box office revenue, the second element refers to the Non-US box office (source: Wikipedia).
# 
# In this exercise, you'll combine all these figures into a single vector. Next, you'll build a matrix from this vector.
# 
# Instructions
# 100 XP
# Use c(new_hope, empire_strikes, return_jedi) to combine the three vectors into one vector. Call this vector box_office.
# Construct a matrix with 3 rows, where each row represents a movie. Use the matrix() function to do this. The first argument is the vector box_office, containing all box office figures. Next, you'll have to specify nrow = 3 and byrow = TRUE. Name the resulting matrix star_wars_matrix.


