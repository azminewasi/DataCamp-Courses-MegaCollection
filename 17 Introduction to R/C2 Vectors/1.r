# 1

# Create a vector
# Feeling lucky? You better, because this chapter takes you on a trip to the City of Sins, also known as Statisticians Paradise!
#   
#   Thanks to R and your new data-analytical skills, you will learn how to uplift your performance at the tables and fire off your career as a professional gambler. This chapter will show how you can easily keep track of your betting progress and how you can do some simple analyses on past actions. Next stop, Vegas Baby. VEGAS!!
#   
#   Instructions
# 100 XP
# Do you still remember what you have learned in the first chapter? Assign the value "Go!" to the variable vegas. Remember: R is case sensitive!

# Define the variable vegas
vegas <- "Go!"



# 2
# 
# Create a vector (2)
# Let us focus first!
#   
#   On your way from rags to riches, you will make extensive use of vectors. Vectors are one-dimension arrays that can hold numeric data, character data, or logical data. In other words, a vector is a simple tool to store data. For example, you can store your daily gains and losses in the casinos.
# 
# In R, you create a vector with the combine function c(). You place the vector elements separated by a comma between the parentheses. For example:
#   
#   numeric_vector <- c(1, 2, 3)
# character_vector <- c("a", "b", "c")
# Once you have created these vectors in R, you can use them to do calculations.
# 
# Instructions
# 100 XP
# Complete the code such that boolean_vector contains the three elements: TRUE, FALSE and TRUE (in that order).
numeric_vector <- c(1, 10, 49)
character_vector <- c("a", "b", "c")

# Complete the code for boolean_vector
boolean_vector <- c(TRUE, FALSE, TRUE)


# 3
# Create a vector (3)
# After one week in Las Vegas and still zero Ferraris in your garage, you decide that it is time to start using your data analytical superpowers.
# 
# Before doing a first analysis, you decide to first collect all the winnings and losses for the last week:
#   
#   For poker_vector:
#   
#   On Monday you won $140
# Tuesday you lost $50
# Wednesday you won $20
# Thursday you lost $120
# Friday you won $240
# For roulette_vector:
#   
#   On Monday you lost $24
# Tuesday you lost $50
# Wednesday you won $100
# Thursday you lost $350
# Friday you won $10
# You only played poker and roulette, since there was a delegation of mediums that occupied the craps tables. To be able to use this data in R, you decide to create the variables poker_vector and roulette_vector.
# 
# Instructions
# 100 XP
# Instructions
# 100 XP
# Assign the winnings/losses for roulette to the variable roulette_vector. You lost $24, then lost $50, won $100, lost $350, and won $10.

# Poker winnings from Monday to Friday
poker_vector <- c(140, -50, 20, -120, 240)

# Roulette winnings from Monday to Friday
roulette_vector <-  c(-24,-50,100,-350,10)
