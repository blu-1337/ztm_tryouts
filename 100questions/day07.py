print("___Question #20:")
# Question 20
# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# Suppose the following input is supplied to the program:

# 7
# Then, the output should be:

# 0
# 7
# 14
# Hints:
# Consider use class, function and comprehension.

class Divisible:
  def __init__(self, iterate_to):
    self.iterate_to = iterate_to
  
  def iterator(self):
    for i in range (0, self.iterate_to+1):
      if i % 7 == 0:
        print(i)
    return "done"

something = Divisible(14)
something.iterator()

print("___Question #21:")
# Question 21
# Question:
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:

# 2
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.Here distance indicates to euclidean distance.Import math module to use sqrt function.

up = int(input("UP "))
down = int(input("DOWN "))
left = int(input("LEFT "))
right = int(input("RIGHT "))

x_movement = abs(up - down)
y_movement = abs(left - right)
if x_movement > y_movement:
  print(x_movement)
else:
  print(y_movement)


