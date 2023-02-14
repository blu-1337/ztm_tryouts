print("___Question #95:")

# Question
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

# If the following string is given as input to the program:

# 5
# 2 3 6 6 5
# Then, the output of the program should be:

# 5
# Hints
# Make the scores unique and then find 2nd best number

input_list = [2,3,6,6,5]
input_number = 5

input_list = list(set(input_list))
print(input_list)
print(input_list[-2])

print("___Question #96:")

# Question
# You are given a string S and width W. Your task is to wrap the string into a paragraph of width.

# If the following string is given as input to the program:

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Then, the output of the program should be:

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ
# Hints
# Use wrap function of textwrap module

import textwrap 

input_text = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
input_number = 4

print(textwrap.TextWrapper(width=input_number).wrap(input_text))



print("___Question #97:")

# Question
# You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:

# #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
# Hints
# First print the half of the Rangoli in the given way and save each line in a list. Then print the list in reverse order to get the rest.


def rangoli(n):
    # your code goes here
    l1=list(map(chr,range(97,123)))
    x=l1[n-1::-1]+l1[1:n]
    mid=len('-'.join(x))
    for i in range(1,n):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(mid,'-'))
    for i in range(n,0,-1):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(mid,'-')) 
rangoli(5)



print("___Question #98:")

# Question
# You are given a date. Your task is to find what the day is on that date.

# Input

# A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

# 08 05 2015
# Output

# Output the correct day in capital letters.

# WEDNESDAY

# Hints
# Use weekday function of calender module

input = "08 05 2015"
input = input.split(" ")
day = int(input[0])
month = int(input[1])
year = int(input[2])

import calendar
calendar_week = calendar.weekday(year, month, day)

if calendar_week == 1:
    print("Monday")
elif calendar_week == 2:
    print("Tuesday")
elif calendar_week == 3:
    print("Wednesday")
elif calendar_week == 4:
    print("Thursday")
elif calendar_week == 5:
    print("Friday")
elif calendar_week == 6:
    print("Saturday")
elif calendar_week == 7:
    print("Sunday")
else:
    print("not a weekday")




print("___Question #99:")

# Question
# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

# Input

# The first line of input contains an integer, M.The second line contains M space-separated integers.The third line contains an integer, N.The fourth line contains N space-separated integers.

# 4
# 2 4 5 9
# 4
# 2 4 11 12
# Output

# Output the symmetric difference integers in ascending order, one per line.

# 5
# 9
# 11
# 12
# Hints
# Use '^' to make symmetric difference operation.

input_list_1 = [2, 4, 5, 9]
input_list_2 = [2, 4, 11, 12]

print(set(input_list_1) ^ set(input_list_2))

