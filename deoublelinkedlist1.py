class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class double_linked_list:

    def __init__(self):
        self.head = None

    def forward_traversal(self):
        if self.head is None:
            print('Double linked list is empty')
        else:
            print('\n Forward Traversal')
            a=self.head
            while a is not None:
                print(a.data,end=' __ ')
                a=a.next

    def backward_traversal(self):
        if self.head is None:
            print('Double linked list is empty')
        else:
            print('\n Backward Traversal')
            a=self.head
            while a.next is not None:
                a=a.next
            while a is not None:
                print(a.data,end=' __ ')
                a=a.prev

    def ins_at_beg(self,data):
        nb=Node(data)
        a=self.head
        a.prev=nb
        nb.next=a
        self.head=nb

    def ins_at_end(self,data):
        ne=Node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ne
        ne.prev=a

    def ins_at_position(self,data,position):
        np=Node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next  
        np.next=a.next
        a.next.prev=np
        a.next=np
        np.prev=a

    def del_at_beg(self):
        a=self.head
        self.head=a.next
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

    def del_at_specefic_position(self,position):
        a=self.head.next
        before=self.head
        for i in range(1,position-1):
            a=a.next
            before=before.next
        before.next=a.next
        a.next.prev=before
        a.next=None
        a.before=None
    
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)

dll=double_linked_list()
dll.head=n1

n1.next=n2
n2.prev=n1

n2.next=n3
n3.prev=n2

n3.next=n4
n4.prev=n3

n4.next=n5
n5.prev=n4

dll.ins_at_beg(1)
dll.ins_at_end(2)
dll.ins_at_position(3,4)
dll.del_at_beg()
dll.del_at_end()
dll.del_at_specefic_position(3)

dll.forward_traversal()
dll.backward_traversal()