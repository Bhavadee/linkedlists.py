class node:
    def __init__ (self,data):
        self.data = data
        self.pref = None
        self.nref = None
class Dll:
    def __init__(self):
        self.head = None
    def insertbegin(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            
        else:
            newnode.nref = self.head
            self.head.pref = newnode
            self.head = newnode
            
           
    def inserlast(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            
        else:
            n = self.head
            while n.nref:
                n = n.nref
            
            n.nref = newnode
            newnode.pref = n
            
    def display(self):
        n  = self.head
        if n != None:
            while(n != None):
                print(n.data)
                n = n.nref
    def insertmid(self,data,pos):
        newnode = node(data)
        if self.head is  None:
            return
        else:
            n = self.head
            i = 0
            while i < (pos -1):
                n = n.nref
                i + 1
            n.nref = newnode
            newnode.pref = n
    def delfirst(self):
        if self.head is None:
            print("Dll is empty")
        else:
            self.head = self.head.nref
            self.head.pref.nref = None
            self.head.pref = None
    def dellast(self):
        if self.head is None:
             print("Dll is empty")
        else:
            n = self.head
            while n.nref:
                n = n.nref
            n.pref.nref = None
    
                
l = Dll()
l.insertbegin(20)
l.insertbegin(10)
l.inserlast(30)
l.inserlast(40)
l.inserlast(50)
l.inserlast(60)
l.delfirst()
l.dellast()
l.dellast()
l.display()
