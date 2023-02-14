print("___Question #90:")

# Question
# Please write a program which count and print the numbers of each character in a string input by console.

# Example: If the following string is given as input to the program:

# abcdefgabc
# Then, the output of the program should be:

# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1
# Hints
# Use dict to store key/value pairs. Use dict.get() method to lookup a key with default value.

input_text = "abcdefgabc"
result = ""
my_dict = {}

formatted_text = [*input_text]
for word in formatted_text:
  if word in my_dict:
    my_dict[word] += 1
  else:
    my_dict[word] = 1

result = my_dict

print(result)

print("___Question #91:")

# Question
# Please write a program which accepts a string from console and print it in reverse order.

# Example: If the following string is given as input to the program:*

# rise to vote sir
# Then, the output of the program should be:

# ris etov ot esir
# Hints
# Use list[::-1] to iterate a list in a reverse order.

input_text = "rise to vote sir"

input_text = input_text[::-1]

print(input_text)

print("___Question #92:")

# Question
# Please write a program which accepts a string from console and print the characters that have even indexes.

# Example: If the following string is given as input to the program:

# H1e2l3l4o5w6o7r8l9d
# Then, the output of the program should be:

# Helloworld
# Hints
# Use list[::2] to iterate a list by step 2.

input_text = 'H1e2l3l4o5w6o7r8l9d'
for i in input_text[::2]:
  print(i, end="")
  print("")



print("___Question #93:")

# Question
# Please write a program which prints all permutations of [1,2,3]

# Hints
# Use itertools.permutations() to get permutations of list.


import itertools
input_list = [1,2,3]

permutations = list(itertools.permutations(input_list))
print(permutations)

print("___Question #94:")

# Question
# Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

# Hints
# Use for loop to iterate all possible solutions.

heads = 35
legs = 94
found = False

for i in range(1, 36):
  j = heads - i
  if 2*i + 4*j == legs:
    print(f"{i} chicken and {j} rabbits")
    found = True
    break
if(not found): 
  print("NOT FOUND!!!")

  
