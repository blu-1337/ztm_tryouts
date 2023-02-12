print("___Question #51:")

# Question
# Write a function to compute 5/0 and use try/except to catch the exceptions.

# Hints
# Use try/except to catch exceptions.

def computer():
  try:
    print(5/0)
  except:
    print("That does not work, bro")

computer()



print("___Question #52:")

# Question
# Define a custom exception class which takes a string message as attribute.

# Hints
# To define a custom exception, we need to define a class inherited from Exception.


class MyCustomError(Exception):
  """This is a custom error class
broooooooooooooooooooooooooooooooooooooooooooooooo"""

  def __init__(self, msg):
    self.msg = msg

  
error = MyCustomError("Something went wrong")



print("___Question #53:")

# Question
# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

# Example: If the following email address is given as input to the program:

# john@google.com
# Then, the output of the program should be:

# john
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# Use \w to match letters.


input_email = "john@google.com"

username = input_email.split("@")[0]
print(username)

# or

import re

email = "john@google.com elise@python.com"
pattern = "(\w+)@\w+.com"
ans = re.findall(pattern,email)
print(ans)