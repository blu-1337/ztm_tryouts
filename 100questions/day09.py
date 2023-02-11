print("___Question #26:")

# Question:
# Define a function which can compute the sum of two numbers.

# Hints:
# Define a function with two numbers as arguments. You can compute the sum in the function and return the value.

def sum_fun(a, b):
  return a + b;

print(sum_fun(3,5))

print("___Question #27:")

# Question:
# Define a function that can convert a integer into a string and print it in console.

# Hints:
# Use str() to convert a number to string.

def int_to_string(integer):
  return str(integer)



print(int_to_string(23), type(int_to_string(23)))

stringed = lambda n : str(n)
print(stringed(21), type(stringed(21)))

print("___Question #28:")

# Question:
# Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.

# Hints:
# Use int() to convert a string to integer.

two_string = lambda s1, s2: int(s1) + int(s2)

print(two_string(12,23))

print("___Question #29:")
# Question:
# Define a function that can accept two strings as input and concatenate them and then print it in console.

# Hints:
# Use + sign to concatenate the strings.

concatenator = lambda s1, s2: s1+s2
print(concatenator("jophn","doe"))

print("___Question #30:")

# Question:
# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

# Hints:
# Use len() function to get the length of a string.


somefun = lambda s1, s2: s1 if(len(s1)>=len(s2)) else s2
print(somefun("titus", "livis"))













