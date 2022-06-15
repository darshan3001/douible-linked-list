from turtle import position

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class doublell:
    def __init__(self):
        self.head = None
    def forward_traversal(self):
        if self.head is None:
            print('list is empty')
        else:
            print()
            print('Forward Traversal : ')
            a=self.head
            while a is not None:
                print(a.data,end=' ____ ')
                a=a.next
    def backward_traversal(self):
        print()
        if self.head is None:
            print('list is empty')
        else:
            print('Backward Traversal : ')
            a=self.head
            while a.next is not None:
                a=a.next
            while a is not None:
                print(a.data,end=' ____ ')
                a=a.prev
    def insert_at_beg(self,data):
        nb=Node(data)
        a=self.head
        a.prev=nb
        nb.next=a
        self.head = nb
    def insert_at_end(self,data):
        ne=Node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ne
        ne.prev=a
    def insert_at_specific_position(self,position,data):
        ns=Node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        ns.prev=a
        ns.next=a.next
        a.next.prev=ns
        a.next=ns
    def del_at_beggining(self):
        a=self.head
        self.head = a.next
        a.next=None
        self.head.prev=None
    def del_at_end(self):
        a=self.head.next
        before=self.head
        while a.next is not None:
            a=a.next
            before=before.next
        before.next=None
        a.prev=None
    def del_at_specific_position(self,position):
        a=self.head.next
        before=self.head
        for i in range(1,position-1):
            a=a.next
            before=before.next
        before.next=a.next
        a.next.prev=before
        a.next=None
        a.prev=None


n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)

dll=doublell()

dll.head=n1

n1.next=n2
n2.prev=n1

n2.next=n3
n3.prev=n2

n3.next=n4
n4.prev=n3

n4.next=n5
n5.prev=n4

dll.insert_at_beg(100)
dll.insert_at_end(200)
dll.insert_at_specific_position(4,300)
dll.insert_at_specific_position(6,400)
dll.del_at_beggining()
dll.del_at_end()
dll.del_at_specific_position(4)

dll.forward_traversal()
dll.backward_traversal()