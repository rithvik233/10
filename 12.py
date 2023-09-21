class Node:
   def __init__(self,data=None):
    self.data = data
    self.next = None
class LinkedList:
   def __init__(self):
    self.first = None
   def insert(self,data):
     temp = Node(data)
     if(self.first):
         current = self.first
         while(current.next):
           current = current.next
         current.next = temp
     else:
       self.first = temp
   def __iter__(self):
      current = self.first
      while current:
        yield current.data
        current = current.next
# Linked List Iterators
ll = LinkedList()
ll.insert(9)
ll.insert(98)
ll.insert("welcome")
ll.insert("govt polytechnic koppal")
ll.insert(456.35)
ll.insert(545)
ll.insert(5)
for x in ll:
   print(x)