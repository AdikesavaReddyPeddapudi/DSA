class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return
        
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

    def insert_at_position(self,data,pos):
        new_node=Node(data)

        if pos==0:
            new_node.next=self.head
            self.head=new_node
            return
        
        temp=self.head
        for i in range(pos-1):
            if temp is None:
                return
            temp=temp.next
        
        if temp is None:
            return
        
        new_node.next=temp.next
        temp.next=new_node

    def delete_from_beginning(self):
        if self.head is None:
            return
        self.head=self.head.next

    def delete_from_ending(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=None
            return  
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None

    def delete_value(self,key):
        if self.head is None:
           return
        if self.head.data==key:
            self.head=self.head.next
            return
        temp=self.head
        while temp.next:
            if temp.next.data==key:
                temp.next=temp.next.next
                return
            temp=temp.next

    def delete_from_position(self,pos):
        if self.head is None:
            return
        
        if pos==0:
            self.head=self.head.next
            return
        
        temp=self.head
        for i in range(pos-1):
            if temp.next  is None:
                return
            temp=temp.next
        
        if temp.next:
            temp.next=temp.next.next

    def search(self,key):
        temp=self.head
        while temp:
            if temp.data==key:
                return True
            temp=temp.next
        return False
    
    def get(self,pos):
        temp=self.head
        for i in range(pos):
            if temp is None:
                return None
            temp=temp.next
        if temp:
            return temp.data
        return None
    
    def reverse(self):
        prev=None
        curr=self.head

        while curr:
            next_node = curr.next     #Store Next Node
            curr.next = prev           #reverse Linked List
            prev = curr                # Move Prev
            curr = next_node           # Move Curr
            
        self.head = prev

    def has_cyclic(self):
        slow=self.head
        fast=self.head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow == fast:
                return True
        return False

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print('None')
'''      
ll=LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_end(40)
ll.insert_at_end(50)
ll.display()
print(ll.search(60))
ll.delete_from_ending()
ll.display()
ll.delete_from_ending()
ll.display()
ll.delete_from_beginning()
ll.display()
ll.insert_at_position(25,1)
ll.insert_at_position(30,2)
ll.insert_at_position(35,3)
ll.insert_at_position(40,4)
ll.display()
ll.insert_at_position(5,0)
ll.display()
ll.delete_from_position(2)
ll.display()
ll.delete_value(30)
ll.display()
print(ll.get(2))
print(ll.get(10))
ll.display()
'''


n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)

# Linking Nodes
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

#Create Cycle
n5.next=n3

# Assign head

ll=LinkedList()
ll.head=n1
print(ll.has_cyclic())
