# To print 'n' terms of  fibonaci series using iteration.

n = int(input("enter the number "))

a, b = 0, 1
count = 0
print a, b
while count < (n - 2):
      c = a + b
      print(c)
      a = b
      b = c
      count += 1
