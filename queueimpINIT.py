class Queue:
    def __init__(self):
        self.Queue = []
    def enqueue(self,item):
        self.Queue.append(item)
    def dequeue(self):
        if len(self.Queue) < 1:
            print('Cant remove an element from an empty queue')
        else:
            return self.Queue.pop(0)
    def display(self):
        print(self.Queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.display()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.display()