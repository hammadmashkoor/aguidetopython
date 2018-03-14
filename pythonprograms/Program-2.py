# To find all prime numbers within a given range

#input from user
high = int(input("Enter upper limit: "))

for a in range(2, high + 1):
    k = 0
    for i in range(2, a // 2 + 1): #use of // for Floor division
        if(a % i == 0):
            k = k + 1
    if(k <= 0):
        print(a)
