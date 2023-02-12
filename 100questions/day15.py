print("___Question #54:")

# Question
# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

# Example: If the following email address is given as input to the program:

# john@google.com
# Then, the output of the program should be:

# google
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# Use \w to match letters.

email = "john@google.com"

result = email.split("@")[1].split(".")
print(result[0])

# or

import re

email = "john@google.com elise@python.com"
pattern = "\w+@(\w+).com"
ans = re.findall(pattern,email)
print(ans)


print("___Question #55:")

# Question
# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

# Example: If the following words is given as input to the program:

# 2 cats and 3 dogs.
# Then, the output of the program should be:

# ['2', '3']
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# Use re.findall() to find all substring using regex.


input_string = "2 cats and 3 dogs."

import re

pattern = "\d"
ans = re.findall(pattern,input_string)
print(ans)

print("___Question #56:")


# Question
# Print a unicode string "hello world".

# Hints
# Use u'strings' format to define unicode string.

input_string = u"hello world"

print(input_string)


print("___Question #57:")

# Question
# Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

# Hints
# Use unicode()/encode() function to convert.

input_ascii = "asdf"
input_ascii = input_ascii.encode("utf-8")
print(input_ascii)

print("___Question #58:")

# Question
# Write a special comment to indicate a Python source code file is in unicode.

# Hints
# Use unicode() function to convert.

# -*- coding: utf-8 -*-


print("___Question #59:")

# Question
# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

# Example: If the following n is given as input to the program:

# 5
# Then, the output of the program should be:

# 3.55
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# Use float() to convert an integer to a float.Even if not converted it wont cause a problem because python by default understands the data type of a value


input_number = 5

sum = 0
for i in range (1, input_number+1):
  sum += i/(i+1)


print(sum)

