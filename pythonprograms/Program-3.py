# To print 'n' terms of  fibonaci series using iteration.

n = int(input("enter the number "))

fib1, fib2 = 0, 1
count = 0
print fib1, fib2
while count < (n - 2):
      fib = fib1 + fib2
      print(fib)
      fib1, fib2 = fib2, fib
      count += 1
