from queue import LifoQueue
stack = LifoQueue()
stack.maxsize = 3
stack.put(1)
stack.put(2)
stack.put(3)
print(stack.qsize())
print(stack.empty())
print(stack.full())