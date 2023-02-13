print("___Question #80:")

# Question
# Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

# Hints
# Use list comprehension to delete a bunch of element from a list.

input_list = [5,6,77,45,22,12,24]
new_list = [i for i in input_list if i % 2 != 0]
print(new_list)

print("___Question #81:")

# Question
# By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

# Hints
# Use list comprehension to delete a bunch of element from a list.

input_list = [12,24,35,70,88,120,155]
new_list = [i for i in input_list if i % 5 == 0 and i % 7 == 0]
print(new_list)

print("___Question #82:")

# Question
# By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

# Hints
# Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.

input_list = [12,24,35,70,88,120,155]
new_list = [i for idx, i in enumerate(input_list) if idx % 2!=0]
print(new_list)


print("___Question #83:")

# Question
# By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

# Hints
# Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.

input_list = [12,24,35,70,88,120,155]
new_list = [i for id, i in enumerate(input_list) if (id!=3) and (id!=5)]
print(new_list)


print("___Question #84:")

# Question
# By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

# Hints
# Use list comprehension to make an array.

array = [[[0 for i in range(0,3)] for j in range (0,5)] for k in range(0,8)]
print(array)

