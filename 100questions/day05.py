print("___Question #16:")

# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:

# 1,2,3,4,5,6,7,8,9
# Then, the output should be:

# 1,9,25,49,81
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


input_value = [1,2,3,4,5,6,7,8,9]

new_list = [x*x for x in input_value if x%2!=0]

print(new_list)

print("___Question #17:")

# Question 17
# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:

# D 300
# D 300
# W 200
# D 100
# Then, the output should be:

# 500


import re

total = 0
while True:
    input_value = input()
    if not input_value:
        break
    if input_value[0] == "W":
      number = int((re.search('[0-9]+', input_value)).group(0))  # group gives the entire match back
      total -= number
      continue
    if input_value[0] == "D":
      number = int((re.search('[0-9]+', input_value)).group(0))  # group gives the entire match back
      total += number
      continue
    print("This is not a valid input. Insert something like D 100 and W 50 to deposit 100 and then withdraw 50")
print("Total is: ", total)

    