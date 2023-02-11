def fibocalc(number):
  if(number == 0):
    return 0
  if(number == 1):
    return 1
  return (fibocalc(number-1)+fibocalc(number-2))


nr = 5
sum = 0
# count = 1

while(nr > 0):
  sum += fibocalc(nr)
  print("aduna: ", fibocalc(nr))
  # count += 1
  nr -= 1

print("suma: ", sum)


def fibocalc2(number):
  if(number == 0):
    return 0
  if(number == 1):
    return 1

  n1 = 0
  n2 =  1
  count = 1

  sum = 1
  while(count < number):
     n = n1 + n2
     n1 = n2
     n2 = n
     count += 1
     sum += n
  

  
  return sum  
  

print("new fibo sum sequence for 5: ", fibocalc2(5))
