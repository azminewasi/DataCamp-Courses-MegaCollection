"""Invalid password
The second part of the website project is to write a script that validates the password entered by the user. The company also puts some rules in order to verify valid passwords:

It can contain lowercase a-z and uppercase letters A-Z
It can contain numbers
It can contain the symbols: *, #, $, %, !, &, .
It must be at least 8 characters long but not more than 20
Your colleague also gave you a list of passwords as examples to test.

The list passwords and the module re are loaded in your session. You can use print(passwords) to view them in the IPython Shell.

Instructions
100 XP
Instructions
100 XP
Write a regular expression to match valid passwords as described.
Scan the elements in the passwords list to find out if they are valid passwords.
To print out the message indicating if it is a valid password or not, complete .format() statement."""

# Write a regex to match a valid password
regex = r"[A-Za-z0-9!#%&*\$\.]{8,20}" 

for example in passwords:
  	# Scan the strings to find a match
    if re.search(regex, example):
        # Complete the format method to print out the result
      	print("The password {pass_example} is a valid password".format(pass_example=example))
    else:
      	print("The password {pass_example} is invalid".format(pass_example=example))     