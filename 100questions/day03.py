print("___Question #10:")


# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

# Suppose the following input is supplied to the program:

# hello world and practice makes perfect and hello world again
# Then, the output should be:

# again and hello makes perfect practice world


# print("enter sequence of whitespace separated words")
# user_input = input()

example_input = "hello world and practice makes perfect and hello world again"

# googled version:
# string1 = example_input
# words = string1.split()
# words.sort()
# result = " ".join(sorted(set(words), key=words.index))

# my version

g_string = example_input.split() 

for word in g_string:
  if g_string.count(word) > 1:
    g_string.remove(word)

g_string.sort()
g_string = " ".join(g_string)
  

print(g_string)

print("___Question #11:")

# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

# Example:

# 0100,0011,1010,1001
# Then the output should be:

# 1010
# Notes: Assume the data is input by console.

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


def convert_binary_to_decimal(number):
  i = 0
  increment = 8
  sum = 0
  while(i < 4):
    if(int(number[i]) == 1):
      sum = sum + increment 
    increment /= 2
    i += 1
  return int(sum)


values = "0100,0011,1010,1001"
values_list = values.split(',')
print(values_list)

for number in values_list:
  if convert_binary_to_decimal(number) % 5 == 0:
    print(number)

