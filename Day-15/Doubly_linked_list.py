from turtle import update


class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    # inserting At The Beginning

    def insert_begin(self,data):
        new_node=Node(data)

        if self.head:
            self.head.prev=new_node
            new_node.next=self.head

        self.head=new_node

    # inserting At The End

    def insert_end(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return
        

        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp

    # inserting at position

    def insert_at_pos(self,pos,data):
        new_node=Node(data)

        if pos == 0:
            self.insert_begin(data)
            return
        temp = self.head
        for _ in range(pos - 1):
            if temp is None:
                return
            temp = temp.next

        if temp.next:
            temp.next.prev=new_node
            new_node.next=temp.next

        temp.next=new_node
        new_node.prev=temp

    # Delete At Beginning

    def delete_begin(self):
        if self.head is None:
            return
        self.head=self.head.next

        if self.head:
            self.head.prev=None
        
    # Delete At End

    def delete_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head=None
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.prev.next= None

    # Delete the Given Value   
    def delete_value(self,key):
        if self.head is None:
            return
        temp=self.head

        while temp:
            if temp.data == key:

                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next:
                    temp.next.prev = temp.next.prev

                return
            temp = temp.next
    
    # Delete At Position
    def delete_at_pos(self,pos):
        if self.head is None:
            return
        temp=self.head

        if pos == 0:
            self.delete_begin()
            return
        
        for _ in range(pos):
            if temp is None:
                return
            temp=temp.next

        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

    # getting element from the given Position
    def get(self,pos):
        temp=self.head

        for _ in range(pos):
            if temp is None:
                return None
            temp = temp.next
        return temp.data if temp else None
    
    # Searching the Element 

    def search(self,key):
        temp=self.head

        while temp:
            if temp.data==key:
                return temp
            temp=temp.next
        return False
    
    # update by Position
    def update(self,pos,value):
        temp=self.head

        for _ in range(pos):
            if temp is None:
                return
        temp=temp.next


        if temp:
            temp.data=value

    # Update by value
    def update_value(self,old,new):
        temp=self.head

        while temp:
            if temp.data == old:
                temp.data = new
            return
        temp=temp.next

    # Display

    def display(self):
        temp=self.head

        while temp:
            print(temp.data,end=' <--> ')
            temp=temp.next
        print('None')


dll=DoublyLinkedList()
dll.insert_begin(10)
dll.insert_begin(20)
dll.display()
dll.insert_end(30)
dll.insert_end(40)
dll.display()
dll.insert_at_pos(3,50)
dll.insert_at_pos(4,60)
dll.insert_at_pos(4,70)
dll.insert_at_pos(6,80)
dll.insert_at_pos(7,90)
dll.display()

dll.delete_begin()
dll.display()
dll.delete_at_pos(2)
dll.display()
dll.delete_end()
dll.display()
dll.delete_value(70)
dll.display()

dll.update(4,100)
dll.display()
dll.update_value(80,85)
dll.display()
dll.get(3)
dll.search(90)

