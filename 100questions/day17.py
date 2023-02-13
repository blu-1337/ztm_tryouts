print("___Question #65:")

# Question
# Please write assert statements to verify that every number in the list [2,4,6,8] is even.

# Hints
# Use "assert expression" to make assertion.

input_list = [2,4,6,8]

for i in input_list:
  assert i % 2 == 0



print("___Question #66:")

# Question
# Please write a program which accepts basic mathematic expression from console and print the evaluation result.

# Example: If the following n is given as input to the program:

# 35 + 3
# Then, the output of the program should be:

# 38
# Hints
# Use eval() to evaluate an expression.

input_string = "35 + 3"

print(eval(input_string))

print("___Question #67:")

# Question
# Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

# Hints
# Use if/elif to deal with conditions.

input_values = [1,2,5,33,44,222,367,666,777,888,2323,3431,23333,239892, 929889, 999121, 1992111] 

def find_value(numbers, number_to_find):
	low = 0
	high = len(numbers) - 1

	while low <= high:
		middle = low + (high - low) // 2  # Divides and returns the integer value of the quotient. It dumps the digits after the decimal.

		if numbers[middle] == number_to_find:
			return middle
		elif numbers[middle] < number_to_find:
			low = middle + 1
		else:
			high = middle - 1
	return -1

print("the values you would like to find has index of: ", find_value(input_values,777))


print("___Question #68:")

# Question
# Please generate a random float where the value is between 10 and 100 using Python module.

# Hints
# Use random.random() to generate a random float in [0,1].

from random import randrange, random
def gen_float():
  return randrange(10,100) + random()

print(gen_float())





print("___Question #69:")

# Question
# Please generate a random float where the value is between 5 and 95 using Python module.

# Hints
# Use random.random() to generate a random float in [0,1].


from random import randrange, random
def gen_float():
  return randrange(5,95) + random()

print(gen_float())
