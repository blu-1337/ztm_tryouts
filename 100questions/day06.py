print("___Question #18:")

# Question 18
# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

# Following are the criteria for checking the password:

# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

# Example

# If the following passwords are given as input to the program:

# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:

# ABd1234@1
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

import re

input_values = 'ABd1234@1,a F1#,2w3E*,2We3345'
password_values = input_values.split(',')

for value in password_values:
  if re.search('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#@$]).{6,12}$', value):
    print("this is a good password: ", value)



print("___Question #19:")

# Question:
# You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:

# 1: Sort based on name
# 2: Then sort based on age
# 3: Then sort by score
# The priority is that name > age > score.

# If the following tuples are given as input to the program:

# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:

# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.We use itemgetter to enable multiple sort keys.

from operator import itemgetter

counter = 0
tuple_list = []
current_tuple = []
while True:
    input_value = input()
    if not input_value:
      tuple_list.append(tuple(current_tuple))
      break
    if counter <= 2:
      current_tuple.append(input_value)    
      counter += 1
      continue
    if counter == 3:
      tuple_list.append(tuple(current_tuple))
      current_tuple = []
      current_tuple.append(input_value)    
      counter = 1
      continue
# print(tuple_list)
sorted_list = sorted_list = sorted(
    tuple_list,
    key=itemgetter(0,1,2),
)


print(sorted_list)



    