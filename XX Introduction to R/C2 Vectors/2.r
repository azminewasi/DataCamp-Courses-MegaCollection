# Naming a vector
# As a data analyst, it is important to have a clear view on the data that you are using. Understanding what each element refers to is therefore essential.
# 
# In the previous exercise, we created a vector with your winnings over the week. Each vector element refers to a day of the week but it is hard to tell which element belongs to which day. It would be nice if you could show that in the vector itself.
# 
# You can give a name to the elements of a vector with the names() function. Have a look at this example:
#   
#   some_vector <- c("John Doe", "poker player")
# names(some_vector) <- c("Name", "Profession")
# This code first creates a vector some_vector and then gives the two elements a name. The first element is assigned the name Name, while the second element is labeled Profession. Printing the contents to the console yields following output:
#   
#   Name     Profession 
# "John Doe" "poker player" 
# Instructions
# 100 XP
# The code in the editor names the elements in poker_vector with the days of the week. Add code to do the same thing for roulette_vector.
# 
# Take Hint (-30 XP)

# Poker winnings from Monday to Friday
poker_vector <- c(140, -50, 20, -120, 240)

# Roulette winnings from Monday to Friday
roulette_vector <- c(-24, -50, 100, -350, 10)

# Assign days as names of poker_vector
names(poker_vector) <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

# Assign days as names of roulette_vector
names(roulette_vector) <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")


# 
# Naming a vector (2)
# If you want to become a good statistician, you have to become lazy. (If you are already lazy, chances are high you are one of those exceptional, natural-born statistical talents.)
# 
# In the previous exercises you probably experienced that it is boring and frustrating to type and retype information such as the days of the week. However, when you look at it from a higher perspective, there is a more efficient way to do this, namely, to assign the days of the week vector to a variable!
#   
#   Just like you did with your poker and roulette returns, you can also create a variable that contains the days of the week. This way you can use and re-use it.
# 
# Instructions
# 100 XP
# A variable days_vector that contains the days of the week has already been created for you.
# Use days_vector to set the names of poker_vector and roulette_vector.

# Poker winnings from Monday to Friday
poker_vector <- c(140, -50, 20, -120, 240)

# Roulette winnings from Monday to Friday
roulette_vector <- c(-24, -50, 100, -350, 10)

# The variable days_vector
days_vector <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

# Assign the names of the day to roulette_vector and poker_vector
names(poker_vector) <- days_vector
names(roulette_vector) <- days_vector

# 
# 
# Calculating total winnings
# Now that you have the poker and roulette winnings nicely as named vectors, you can start doing some data analytical magic.
# 
# You want to find out the following type of information:
#   
#   How much has been your overall profit or loss per day of the week?
#   Have you lost money over the week in total?
#   Are you winning/losing money on poker or on roulette?
#   To get the answers, you have to do arithmetic calculations on vectors.
# 
# It is important to know that if you sum two vectors in R, it takes the element-wise sum. For example, the following three statements are completely equivalent:
#   
#   c(1, 2, 3) + c(4, 5, 6)
# c(1 + 4, 2 + 5, 3 + 6)
# c(5, 7, 9)
# You can also do the calculations with variables that represent vectors:
#   
#   a <- c(1, 2, 3) 
# b <- c(4, 5, 6)
# c <- a + b
# Instructions
# 100 XP
# Take the sum of the variables A_vector and B_vector and assign it to total_vector.
# Inspect the result by printing out total_vector.

A_vector <- c(1, 2, 3)
B_vector <- c(4, 5, 6)

# Take the sum of A_vector and B_vector
total_vector <- A_vector + B_vector

# Print out total_vector
total_vector
# 
# 
# Calculating total winnings (2)
# Now you understand how R does arithmetic with vectors, it is time to get those Ferraris in your garage! First, you need to understand what the overall profit or loss per day of the week was. The total daily profit is the sum of the profit/loss you realized on poker per day, and the profit/loss you realized on roulette per day.
# 
# In R, this is just the sum of roulette_vector and poker_vector.
# 
# Instructions
# 100 XP
# Assign to the variable total_daily how much you won or lost on each day in total (poker and roulette combined).

# Poker and roulette winnings from Monday to Friday:
poker_vector <- c(140, -50, 20, -120, 240)
roulette_vector <- c(-24, -50, 100, -350, 10)
days_vector <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
names(poker_vector) <- days_vector
names(roulette_vector) <- days_vector

# Total winnings with poker
total_poker <- sum(poker_vector)

# Total winnings with roulette
total_roulette <-  sum(roulette_vector)

# Total winnings overall
total_week <- total_poker+total_roulette

# Print out total_week
total_week