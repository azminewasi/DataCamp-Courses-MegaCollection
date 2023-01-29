"""Computing & plotting
Now that you've got the entire delayed pipeline prepared it's time compute and plot the result. Matplotlib has been imported for you as plt.

Warning: The execution of of this exercise is expected to be several seconds.

Instructions
100 XP
Perform the computation on result and assign it to tip_frac.
Print the type of tip_frac.
Hit 'Submit Answer to view the plot."""

# Perform the computation
tip_frac = result.compute()
# Print the type of tip_frac
print(type(tip_frac))

# Generate a line plot using .plot.line()
tip_frac.plot.line()
plt.ylabel('Tip fraction')
plt.show()