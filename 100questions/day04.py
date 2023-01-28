print("___Question #12:")


input_value = "Hello world!"

lower_case_letters = 0
upper_case_letters = 0

for char in input_value:
  if char.isalpha():  # this checks if it's a letter or not
    if char.islower():
      lower_case_letters += 1
    if char.isupper():
      upper_case_letters += 1




print("Lower case letters: ", lower_case_letters)
print("Upper case letters: ", upper_case_letters)
