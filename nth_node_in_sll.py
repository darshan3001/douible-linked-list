class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class singlyll:

    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print('List is empty')
        else:
            a = self.head
            while a is not None:
                print(a.data, end = ' --> ')
                a = a.next

    def insert_at_beginning(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
    
    def nth_node(self,index):
        a=self.head
        count=0
        while a:
            if (count==index):
                return a.data
            a=a.next
            count+=1


n1=Node(5)
n2 =Node(10)
n3 = Node(15)
n4 = Node(20)
n5 = Node(25)
sll = singlyll()
sll.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
sll.insert_at_beginning(1)
sll.nth_node(10)
sll.traversal()