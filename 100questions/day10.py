print("___Question #31:")

# Question:
# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.

def print_dict():
  some_dic = {}
  for i in range(1, 21):
    some_dic[i] = i**2
  return some_dic

print(print_dict())

print("___Question #32:")

# Question:
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

def print_dict():
  some_dic = {}
  for i in range(1, 21):
    some_dic[i] = i**2
    print(i)
  return some_dic

print(print_dict())

print("___Question #33:")

# Question:
# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.

def print_list():
  some_list = []
  for i in range(1, 21):
    some_list.append(i**2)
    # print(i)
  return some_list

print(print_list())

print("___Question #34:")

# Question:
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list

def print_list():
  some_list = []
  for i in range(1, 21):
    some_list.append(i**2)
    # print(i)
  return some_list

print(print_list())


print("___Question #35:")

# Question:
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list

def print_list():
  some_list = []
  for i in range(1, 21):
    some_list.append(i**2)
    if i > 15:
      print(some_list[i-1])
  return some_list

print_list()


print("___Question #36:")

# Question:
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

# Hints: Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list
# Main Author's Solution: Python 2


def print_list():
  some_list = []
  for i in range(1, 21):
    some_list.append(i**2)
    if i > 5:
      print(some_list[i-1])
  return some_list

print_list()

print("___Question #37:")

# Question:
# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use tuple() to get a tuple from a list. 

def print_list():
  some_list = []
  for i in range(1, 21):
    some_list.append(i**2)
    # if i > 5:
    #   print(some_list[i-1])
  return tuple(some_list)


print(print_list())