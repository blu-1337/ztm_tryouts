print("___Question #22:")
# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

# Suppose the following input is supplied to the program:

# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:

# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
# Hints
# In case of input data being supplied to the question, it should be assumed to be a console input.


input_text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
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


print("___Question #23:")
# Question:
# Write a method which can calculate square value of number

# Hints:
# Using the ** operator which can be written as n**p where means n^p

class Squareable(): 
  
  def __init__(self, value):
    self.value = value
  def squared(self):
    print("squared is: ", int(self.value)**2)

x = Squareable(20)
x.squared()


print("___Question #24:")
# Question:
# Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.

# Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

# And add document for your own function

# Hints:
# The built-in document method is __doc__

print(abs.__doc__)
print(int.__doc__)
# print(raw_input.__doc__)  # does not work

class MyNiceMethod():
  """This is some nice method documentation
on multiple lines even
how bout that"""

x = MyNiceMethod()
print(x.__doc__)



print("___Question #25:")

# Question:
# Define a class, which have a class parameter and have a same instance parameter.

# Hints:
# Define an instance parameter, need add it in __init__ method.You can init an object with construct parameter or set the value later

class ThatClass():
  name = "Cara"

  def __init__(self, name = "Unnamed"):
    self.name = name
    print("I am myself, I guess.")


boy = ThatClass()
girl = ThatClass("Tiffany")
print(boy.name)
print(girl.name)
print(ThatClass.name)