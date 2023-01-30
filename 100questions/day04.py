print("___Question #14:")

# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Suppose the following input is supplied to the program:

# Hello world!
# Then, the output should be:

# UPPER CASE 1
# LOWER CASE 9
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


input_value = "Hello world!"

lower_case_letters = 0
upper_case_letters = 0

for char in input_value:
  if char.isalpha():  # this checks if it's a letter or not
    if char.islower():
      lower_case_letters += 1
    if char.isupper():
      upper_case_letters += 1




print("Lower case letters: ", lower_case_letters)
print("Upper case letters: ", upper_case_letters)


print("___Question #15:")

# Question 15
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

# Suppose the following input is supplied to the program:

# 9
# Then, the output should be:

# 11106
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

input_value = 9

sum = 0
for i in range(1,5):
  number = ""
  while i>=1:
    number += str(input_value)
    print(number)
    i -= 1
  sum += int(number)
print(sum)

