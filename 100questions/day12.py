print("___Question #44:")

# Question:
# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

# Hints:
# Use map() to generate a list. Use lambda to define anonymous functions.

result = map(lambda x: x**2, range(1,21))

print(list(result))

print("___Question #45:")

# Question:
# Define a class named American which has a static method called printNationality.

# Hints:
# Use @staticmethod decorator to define class static method.There are also two more methods.To know more, go to this link.

class American():
  def print_nationality(self):
    print("I am american")

    

citizen = American()
citizen.print_nationality()

print("___Question #46:")


# Question:
# Define a class named American and its subclass NewYorker.

# Hints:
# Use class Subclass(ParentClass) to define a subclass.*

class American():
  def print_nationality(self):
    print("I am american")

class NewYorker(American):
  def print_nationality(self):
    print("I am american, but I come from New York!")
  
citizen = NewYorker()
citizen.print_nationality()  # prints "I am american, but I come from New York!"