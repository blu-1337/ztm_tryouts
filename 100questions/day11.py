print("___Question #38:")

# Question:
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

# Hints:
# Use [n1:n2] notation to get a slice from a tuple.

given_tuple = (1,2,3,4,5,6,7,8,9,10)

print(given_tuple[0:5])
print(given_tuple[5:10])

print("___Question #39:")

# Question:
# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

# Hints:
# Use "for" to iterate the tuple. Use tuple() to generate a tuple from a list.

new_tuple_list = []
for elem in given_tuple:
  if elem % 2 == 0:
    print(elem)
    new_tuple_list.append(elem)
new_tuple_list = tuple(new_tuple_list)

print(new_tuple_list)

print("___Question #40:")

# Question:
# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

# Hints:
# Use if statement to judge condition.


user_input = input("write YES: ")

if user_input == "Yes" or user_input == "YES" or user_input == "yes":
  print("YES!")
else:
  print("NO!")

print("___Question #41:")

# Question 41
# Question:
# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.Use lambda to define anonymous functions.


initial_list = [1,2,3,4,5,6,7,8,9,10]

result = list(map(lambda x : x**2, initial_list))

print(result)

print("___Question #42:")

# Question:
# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.Use filter() to filter elements of a list.Use lambda to define anonymous functions.

initial_list = [1,2,3,4,5,6,7,8,9,10]

# result = list(filter(lambda x: True if (x%2==0) else False, map(lambda x : x**2, initial_list)))

result = list(map(lambda x: x**2, filter(lambda x: x%2==0, initial_list)))

print(result)

print("___Question #43:")

# Question:
# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

# Hints:
# Use filter() to filter elements of a list.Use lambda to define anonymous functions.


result = list(map(lambda x: x**2, filter(lambda x: x%2==0, range(1,21))))

print(result)