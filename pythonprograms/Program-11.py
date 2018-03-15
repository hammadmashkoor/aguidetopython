""" Program-11 : To implement stack using list"""
from sys import maxsize

stack= ['hello', 'red','white','green', 'gold']
n=input("Enter a - Push and b- Pop")
""""
def createStack():
    stack=[]
    return stack
"""
def isEmpty(stack):
    return len(stack)==0

def push(stack, item):
    stack.append(item)
    print("Push to stack "+item)

def pop(stack):
    if isEmpty(stack):
        return str(maxmize-1)

    return print(stack.pop())

def stackIn(n, stack):
    if n == 'a':
        item =input("Item to push into the stack")
        return push(stack, item)
    elif n == 'b':
        return pop(stack)
    else:
        return print("Not a proper input for push & pop ")

stackIn(n, stack)



