class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class singlyll():
    def __init__(self):
        self.head = None
    def traversal(self):
        if self.head is None:
            print('list i sempty')
        else:
            a = self.head
            while a is not None:
                print(a.data,end = '-->')
                a=a.next
    def insertion_at_beginnning(self,data):
        nb = node(data)
        nb.next = self.head
        self.head = nb
    def insertion_at_end(self,data):
        ne = node(data)
        a = self.head
        while a.next is not None:
            a=a.next
        a.next = ne

sll=singlyll()
sll.insertion_at_beginnning(2)
sll.insertion_at_beginnning(4)
sll.insertion_at_beginnning(6)
sll.insertion_at_end(7)
sll.traversal()
