class Stack:
    def __init__ (self):
        self.Stack = []
    def insert(self,item):
        self.Stack.append(item)
    def delete(self):
        if len(self.Stack) < 1:
            print('Cant delete the element from an empty Stack')
        else:
            return self.Stack.pop()
    def display(self):
        print(self.Stack)

s = Stack()
s.insert(1)
s.insert(2)
s.insert(3)
s.insert(4)
s.display()
s.delete()
s.delete()
s.display()
