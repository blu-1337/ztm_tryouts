print("___Question #85:")

# Question
# By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

# Hints
# Use list comprehension to delete a bunch of element from a list.Use enumerate() to get (index, value) tuple.


input_list = [12,24,35,70,88,120,155]
new_list = [i for id, i in enumerate(input_list) if (id!=0) and (id!=4) and (id!=5)]
print(new_list)


print("___Question #86:")

# Question
# By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

# Hints
# Use list's remove method to delete a value.

input_list = [12,24,35,70,88,120,155]
input_list.remove(24)
print(input_list)

print("___Question #87:")

# Question
# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

list_1 = [1,3,6,78,35,55]
list_2 = [12,24,35,24,88,120,155]
set_1 = set(list_1)
set_2 = set(list_2)
combined_list = list(set_1.intersection(set_2))
print(combined_list)

# Hints
# Use set() and "&=" to do set intersection operation.

print("___Question #88:")

# Question
# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

# Hints
# Use set() to store a number of values without duplicate.

input_list = [12,24,35,24,88,120,155,88,120,155]
# input_list = list(set(input_list))
# print(input_list)
for i in input_list:
  if input_list.count(i)>1:
    input_list.remove(i)
print(input_list)


print("___Question #89:")

# Question
# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

# Hints
# Use Subclass(Parentclass) to define a child class.

class Person():
  pass

class Male(Person):
  def getGender(self):
    print("Male")

class Female(Person):
  def getGender(self):
    return "Female"

cat = Female()
print(cat.getGender())




