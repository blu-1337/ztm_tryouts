print("___Question #4:")

# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list
# and a tuple which contains every number.Suppose the following input is supplied to the program:
#
# 34,67,55,33,12,98
# Then, the output should be:
#
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

input_nrs = "34,67,55,33,12,98"

print(tuple(input_nrs.split(',')))

print("___Question #5:")

# Question:
# Define a class which has at least two methods:
#
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#
# Hints:

# class MyClass():
#
#     def getString(self):
#         self.input = input("Inser your string: ")
#     def printString(self):
#         print(self.input.upper())
#
# cat = MyClass()
# cat.getString()
# cat.printString()

print("___Question #6:")

# Question:
# Write a program that calculates and prints the value according to the given formula:
#
# Q = Square root of [(2 _ C _ D)/H]
#
# Following are the fixed values of C and H:
#
# C is 50. H is 30.
#
# D is the variable whose values should be input to your program in a comma-separated sequence.
# For example Let us assume the following comma separated input sequence is given to the program:
#
# 100,150,180
# The output of the program should be:
#
# 18,22,24
from math import sqrt

C = 50
H = 30
D = [100,150,180]
# Q = sqrt(2*C*D)/H

print(list(map(lambda x: int(sqrt(2*C*x/H)), D)))


print("___Question #7:")


# Question:
# _Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i _ j.*
#
# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
#
# Then, the output of the program should be:
#
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

x = 3
y = 5
new_array = []
for i in range (0,x):
    j_array = []
    for j in range (0,y):
        j_array.append(i*j)
    new_array.append(j_array)
print(new_array)

print("___Question #8:")

# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a
# comma-separated sequence after sorting them alphabetically.
#
# Suppose the following input is supplied to the program:
#
# without,hello,bag,world
# Then, the output should be:
#
# bag,hello,without,world

input_words = "without,hello,bag,world"

input_words = list(input_words.split(','))

print(input_words)

input_words.sort()

print(input_words)



print("___Question #9:")

# Write a program that accepts sequence of lines as input and prints the lines after making
# all characters in the sentence capitalized.
#
# Suppose the following input is supplied to the program:
#
# Hello world
# Practice makes perfect
# Then, the output should be:
#
# HELLO WORLD
# PRACTICE MAKES PERFECT

lines = []
while True:
    input_sentance = input()

    # 👇️ if user pressed Enter without a value, break out of loop
    if input_sentance == '':
        break
    else:
        lines.append(input_sentance.upper() + '\n')

for word in lines:
    print(word)


