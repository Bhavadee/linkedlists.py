class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class linkedlist:
    def _init_(self):
        self.head = None
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next
                
    def insertafter(self,data,x):
        new_node = node(data)
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        new_node.next = n.next
        n.next = new_node
    def insertbefore(self,data,x):

        if self.head is None:
            print("ll is empty")
        if self.head == x:
            new_node = node(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
              break
            n = n.next
            if n.next is None:
                print("not defined:")
            else:
                new_node = node(data)
                new_node.next = n.next
                n.next = new_node
             
     
        
    def addstart(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
    def addend(self,data):
        new_nodes = node(data)
        if self.head is None:
            self.head = new_nodes
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_nodes
L = linkedlist()
n = node(10)
L.head = n
n1 = node(20)
n.next = n1
n2 = node(30)
n1.next = n2
L.addend(890)
L.addstart(5)
L.insertafter(25,20)
L.insertafter(25,20)
L.display()
