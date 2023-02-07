print("___Question #22:")
# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

# Suppose the following input is supplied to the program:

# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:

# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
# Hints
# In case of input data being supplied to the question, it should be assumed to be a console input.


input_text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
result = ""
my_dict = {}

formatted_text = input_text.split(" ")
for word in formatted_text:
  if word in my_dict:
    my_dict[word] += 1
  else:
    my_dict[word] = 1

result = my_dict

print(result)
print("___Question #23:")
print("___Question #24:")
print("___Question #25:")
