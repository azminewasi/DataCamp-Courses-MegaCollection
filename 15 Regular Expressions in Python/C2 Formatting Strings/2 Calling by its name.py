"""Calling by its name
You have created your database with the tools and the different Data Science subfields they are used in. The company is considering creating courses using these tools and sending personalized emails to the users recommending the different topics. They have asked you to make this process more time-efficient. To do this, you want to create a template email with a standard message changing the different tools and corresponding field name.

First, you want to try doing this with just one example as a proof of concept. You use positional formatting and named placeholders to call the variables in a dictionary.

The variable courses containing one tool and one field name has been saved. You can use print(courses) to view the variable in the IPython Shell."""

# Create a dictionary
plan = {
  		"field": courses[0],
        "tool": courses[1]
        }

# Complete the placeholders accessing elements of field and tool keys in the data dictionary
my_message = "If you are interested in {data[field]}, you can take the course related to {data[tool]}"

# Use the plan dictionary to replace placeholders
print(my_message.format(data=plan))