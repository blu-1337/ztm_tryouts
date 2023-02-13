print("___Question #70:")

# Question
# Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

# Hints
# Use random.choice() to a random element from a list.


import random

random_list = random.sample(range(0,11),10)

print(random_list)
print("random element from above list:", random.choice(random_list))

print("___Question #71:")

# Question
# Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension.

# Hints
# Use random.choice() to a random element from a list.

random_list = [i for i in range(10,151) if i % 5 == 0 and i % 7 == 0]
# print(random_list)



print(random.sample(random_list, 1))  # picks one number from the list
 
# print(random_list)


print("___Question #72:")

# Question
# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

# Hints
# Use random.sample() to generate a list of random values.

random_list = []

for i in range(0,5): 
  element =  random.randrange(100, 201)
  random_list.append(element)

print(random_list)

print("___Question #73:")

# Question
# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

# Hints
# Use random.sample() to generate a list of random values.

random_list = []

for i in range(0,5): 
  while(True):
    element =  random.randrange(100, 201)
    if element % 2 == 0:
      random_list.append(element)
      break


print(random_list)


print("___Question #74:")

# Question
# Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

# Hints
# Use random.sample() to generate a list of random values.


random_list = []

for i in range(0,5): 
  while(True):
    element =  random.randrange(1, 1001)
    if element % 5 == 0 and element % 7 == 0:
      random_list.append(element)
      break


print(random_list)

