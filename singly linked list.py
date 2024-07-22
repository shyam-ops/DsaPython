#Define a class Node to describe a node of a singly linked list.
class Node:
    def __init__(self,item=None , next=None):
        self.item = item
        self.next = next
#Define a class SLL to implement Singly Linked List with __init__() method to create and initialise start reference variable.
class SLL:
    def __init__(self,start=None):
        self.start=start
#Define a method is_empty() to check if the linked list is empty in SLL class.
    def is_empty(self):
        return self.start == None
#In class SLL, define a method insert_at_start() to insert an element at the starting of the list.
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
#In class SLL, define a method insert_at_last() to insert an element at the end of the list.
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start = n
#In class SLL, define a method search() to find the node with specified element value.
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
#In class SLL, define a method insert_after() to insert a new node after a given node of the list.
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
#In class SLL, define a method to print all the elements of the list.
    def print_all(self):
        temp=self.start
        while temp is not None:
            print(temp.item , end = ' ')
            temp=temp.next

#driver code
mylist = SLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.search(20)
mylist.insert_after(mylist.search(20),30)
mylist.print_all()