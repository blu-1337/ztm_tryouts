print("___Question #60:")

# Question
# Write a program to compute:

# f(n)=f(n-1)+100 when n>0
# and f(0)=0
# with a given n input by console (n>0).

# Example: If the following n is given as input to the program:

# 5
# Then, the output of the program should be:

# 500
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# We can define recursive function in Python.

input_n = 5

def calculate(n):
  if n == 0:
    return 0
  else: 
    return calculate(n-1)+100

print(calculate(input_n))



print("___Question #61:")

# Question
# The Fibonacci Sequence is computed based on the following formula:

# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by console.

# Example: If the following n is given as input to the program:

# 7
# Then, the output of the program should be:

# 13
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# We can define recursive function in Python.

def fibocalc(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibocalc(n-1)+fibocalc(n-2)

print(fibocalc(7))  




print("___Question #62:")

# Question
# The Fibonacci Sequence is computed based on the following formula:

# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by console.

# Example: If the following n is given as input to the program:

# 7
# Then, the output of the program should be:

# 0,1,1,2,3,5,8,13
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# We can define recursive function in Python. Use list comprehension to generate a list from an existing list. Use string.join() to join a list of strings.



def fibocalc2(n):
  result = []
  if n == 0:
    result.append(0)
    return result
  if n == 1:
    result.append(0)
    result.append(1)
    return result
  result = [0,1]
  for i in range(2,n+1):
    fib = result[-1] + result[-2]
    result.append(fib)
  return result

print(fibocalc2(7))  



print("___Question #63:")

# Question
# Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

# Example: If the following n is given as input to the program:

# 10
# Then, the output of the program should be:

# 0,2,4,6,8,10
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# Use yield to produce the next value in generator.


def gen(n):
  result_list = []
  for i in range(0,n+1):
    if i%2==0:
      result_list.append(i)
  return result_list


print(gen(10))

print("___Question #64:")

# Question
# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

# Example: If the following n is given as input to the program:

# 100
# Then, the output of the program should be:

# 0,35,70
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# Use yield to produce the next value in generator.


def gen(n):
  result_list = []
  for i in range(0,n+1):
    if i%5==0 and i%7==0:
      result_list.append(i)
  return result_list


print(gen(100))