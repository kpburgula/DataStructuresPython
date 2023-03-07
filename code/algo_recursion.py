def factorial(n):
  if n == 0:
    return 1
  else:
    while(n==1):
      return 1
    
    fact = n * factorial(n-1)

  return fact

print(factorial(0))


#Fibonacci : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
counter = 0
curr_num = 0
next_num = 1
sum = 1
def fibonacci(n):
  

  while (counter == n):
    return sum
  curr_num = next_num
  next_num = sum
  counter+=1
  sum = fibonacci(n)
  return sum

print(fibonacci(3))

  
