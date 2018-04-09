""" Program-12 : To implement queue using list"""
from collections import deque
# declaration of queue
queue = deque(["Ram","Tarun","Asif","John"])
print(queue)

# Adding Element in queue
queue.append("Akber")
print(queue)
queue.append("Birbal")
print(queue)

# Deleting element from the queue
print(queue.popleft())
print(queue.popleft())
print(queue)                