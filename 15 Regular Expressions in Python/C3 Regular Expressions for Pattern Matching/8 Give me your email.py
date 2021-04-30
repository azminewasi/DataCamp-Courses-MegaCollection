"""Give me your email
A colleague has asked for your help! When a user signs up on the company website, they must provide a valid email address.
The company puts some rules in place to verify that the given email address is valid:

The first part can contain:
Upper A-Z and lowercase letters a-z
Numbers
Characters: !, #, %, &, *, $, .
Must have @
Domain:
Can contain any word characters
But only .com ending is allowed
The project consist of writing a script that checks if the email address follow the correct pattern. Your colleague gave you a list of email addresses as examples to test.

The list emails as well as the re module are loaded in your session. You can use print(emails) to view the emails in the IPython Shell.

Instructions
100 XP
Instructions
100 XP
Write a regular expression to match valid email addresses as described.
Match the regex to the elements contained in emails.
To print out the message indicating if it is a valid email or not, complete .format() statement."""

# Write a regex to match a valid email address
regex = r"[A-Za-z0-9!#%&*\$\.]+@\w+\.com"

for example in emails:
  	# Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
      	print("The email {email_example} is a valid email".format(email_example=example))
    else:
      	print("The email {email_example} is invalid".format(email_example=example))   