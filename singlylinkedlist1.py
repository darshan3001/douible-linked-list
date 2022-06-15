class node():
    def __init__(self,data):
        self.data = data
        self.next = None
class singlyll():
    def __init__(self):
        self.head = None
    def traversal(self):
        if self.head is None:
            print('list is empty')
        else:
            a = self.head
            while a is not None:
                print(a.data,end = ' --> ')
                a = a.next
    def insert_at_beginning(self,data):
        nb = node(data)
        nb.next = self.head
        self.head = nb
    def insert_at_end(self,data):
        ne = node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next = ne
    def insert_node_at_specified_position(self,position,data):
        nib = node(data)
        a = self.head
        for i in range(1,position - 1):
            a=a.next
        nib.next = a.next
        a.next = nib  
    def deletion_at_beginning(self):
        a = self.head
        self.head = a.next
        a.head = None
    def deletion_at_ending(self):
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a=a.next
            prev = prev.next
        prev.next = None
    def deletion_at_specified_position(self,position):
        prev = self.head
        a = self.head.next
        for i in range(1, position-1):
            a=a.next
            prev = prev.next
        prev.next = a.next
        a.next = None
n1 = node(1)
n2 = node(3)
n3 = node(5)
n4 = node(7)
n5 = node(9)
sll = singlyll()
sll.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
sll.insert_at_beginning(0)
sll.insert_at_beginning(-1)
sll.insert_at_end(11)
sll.insert_node_at_specified_position(3,'3rd')
sll.deletion_at_beginning()
sll.deletion_at_ending()
sll.deletion_at_specified_position(2)
sll.traversal()