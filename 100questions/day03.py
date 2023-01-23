print("___Question #5:")


# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

# Suppose the following input is supplied to the program:

# hello world and practice makes perfect and hello world again
# Then, the output should be:

# again and hello makes perfect practice world


# print("enter sequence of whitespace separated words")
# user_input = input()

example_input = "hello world and practice makes perfect and hello world again"

# googled version:
# string1 = example_input
# words = string1.split()
# words.sort()
# result = " ".join(sorted(set(words), key=words.index))

# my version

g_string = example_input.split() 

for word in g_string:
  if g_string.count(word) > 1:
    g_string.remove(word)

g_string.sort()
g_string = " ".join(g_string)
  

print(g_string)

