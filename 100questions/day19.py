print("___Question #75:")

# Question
# Please write a program to randomly print a integer number between 7 and 15 inclusive.

# Hints
# Use random.randrange() to a random integer in a given range.

import random

print(random.randrange(7,16))

print("___Question #76:")

# Question
# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

# Hints
# Use zlib.compress() and zlib.decompress() to compress and decompress a string.

import zlib

input_string = "hello world!hello world!hello world!hello world!"

compressed = zlib.compress(input_string.encode())
print(compressed)
print(zlib.decompress(compressed))


print("___Question #77:")

# Question
# Please write a program to print the running time of execution of "1+1" for 100 times.

# Hints
# Use timeit() function to measure the running time.




import datetime

before = datetime.datetime.now()
for i in range(100):
    x = 1 + 1
after = datetime.datetime.now()
execution_time = after - before
print(execution_time.microseconds)

print("___Question #78:")

# Question
# Please write a program to shuffle and print the list [3,6,7,8].

# Hints
# Use shuffle() function to shuffle a list.

input_list = [3,6,7,8]

import random

random.shuffle(input_list)
print(input_list)

print("___Question #79:")

# Question
# Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

# Hints
# Use list[index] notation to get a element from a list.


subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey","Football"]

for subject in subjects:
  for verb in verbs:
    for object in objects:
      print(subject, verb, object)
    
