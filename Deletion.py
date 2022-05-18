class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def delete_first(self):
        if self.head is None:
            print("list is empty")
            #temp=self.head
        else:
            self.head=self.head.next

    def delete_mid(self,pos):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            i=1
            while(i<(pos)):
                pre=temp
                temp=temp.next
                i=i+1
            pre.next=temp.next
            
    def delete_last(self):
            if self.head is None:
                print("list is empty")
            else:
                temp=self.head
                while temp.next:
                    pre=temp
                    temp=temp.next
                pre.next=None
            

    def display(self):
        if self.head is None:
            #print("list is empty")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, "-->", end=' ')
                temp = temp.next

    
L = linkedlist()
n = node(10)
L.head = n
n1 = node(20)
n.next = n1
n2 = node(30)
n1.next = n2
n3= node(40)
n2.next = n3
n4= node(50)
n3.next = n4
L.delete_first()
L.delete_last()
L.delete_mid(2)
L.display ()         
            
                
