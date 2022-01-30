from ast import Delete


class Node:
    def __init__(self,item):
        self.item=item
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    
    def Atbeg(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def Atlast(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
    def Delete(self,data):
        if self.head is None:
            return
        temp=

