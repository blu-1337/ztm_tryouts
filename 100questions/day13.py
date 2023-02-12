print("___Question #47:")


# Question
# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

# Hints
# Use def methodName(self) to define a method.

class Circle():
  def __init__(self, radius):
    self.radius = int(radius)
    print("nigga", radius)
  def radius_calc(self):
    return 3.147 * self.radius ** 2

my_circle = Circle(112)

print(my_circle.radius_calc())
# my_circle.radius()

print("___Question #48:")

# Question
# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

# Hints
# Use def methodName(self) to define a method.

class Rectangle():
  def __init__(self, length, width):
    self.length = length
    self.width = width
  def calculate_area(self):
    return self.length * self.width

my_rect = Rectangle(10,20)

print(my_rect.calculate_area())

print("___Question #49:")

# Question
# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

# Hints
# To override a method in super class, we can define a method with the same name in the super class.



class Shape():
  def __init__(self):
    pass
  def area(self):
    return 0

class Square(Shape):
  def __init__(self, length):
    self.length = length
    pass
  def area(self):
    return self.length ** 2

square = Square(11)
print(square.area())


print("___Question #50:")

# Question
# Please raise a RuntimeError exception.

# Hints
# UUse raise() to raise an exception.

raise RuntimeError("something went terribly wrong")