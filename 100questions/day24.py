print("___Question #100:")

# Question
# You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

# If the following string is given as input to the program:

# 4
# bcdef
# abcdefg
# bcde
# bcdef
# Then, the output of the program should be:

# 3
# 2 1 1
# Hints
# Make a list to get the input order and a dictionary to count the word frequency

input_text = "bcdef abcdefg bcde bcdef"
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

print("___Question #101:")

# Question
# You are given a string. Your task is to count the frequency of letters of the string and print the letters in descending order of frequency.

# If the following string is given as input to the program:

# aabbbccde
# Then, the output of the program should be:

# b 3
# a 2
# c 2
# d 1
# e 1
# Hints
# Count frequency with dictionary and sort by Value from dictionary Items

input_text = "aabbbccde"
result = ""
my_dict = {}

formatted_text = [*input_text]
for word in formatted_text:
  if word in my_dict:
    my_dict[word] += 1
  else:
    my_dict[word] = 1

result = my_dict  # this is not properly sorted


print(result)


print("___Question #102:")

# Question
# Write a Python program that accepts a string and calculate the number of digits and letters.

# Input

# Hello321Bye360
# Output

# Digit - 6
# Letter - 8
# Hints
# Use isdigit() and isalpha() function

input_text = "Hello321Bye360"
formatted_text = [*input_text]
digits = 0
letter = 0
for char in formatted_text:
  if char.isdigit():
    digits += 1
  else:
    letter += 1
print(f"{digits} digits and {letter} letters!")


print("___Question #103:")

# Question
# Given a number N.Find Sum of 1 to N Using Recursion

# Input

# 5
# Output

# 15
# Hints
# Make a recursive function to get the sum

def summer(n):
  if n == 0:
    return 0
  return n+summer(n-1)

print(summer(5))