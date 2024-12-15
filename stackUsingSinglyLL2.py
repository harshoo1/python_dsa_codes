""" stack using inheriting the linked list class 
singly ll as parent class and stack as child class"""

from sll_package.sll_class import *
 
 #1. defining stack class
class Stack:
    def __init__(self):
        self.mylist = SinglyLL()
        self.value_count = 0
#2. is_empty() ?
    def is_empty(self):
        self.mylist.isEmpty()
#3. push data
    def push(self,data):
        self.mylist.insertAtStart(data)
        self.value_count += 1
#4. pop data
    def pop(self):
        if not self.is_empty():
            self.mylist.deleteFirstNode()
            self.value_count -= 1
#5. peek 
    def peek(self):
        if not self.is_empty():
            return self.mylist.value
#6. size
    def size(self):
        return self.value_count         
   

#main code
stack1 = Stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.push(40)
stack1.push(50)


print(stack1.peek())
stack1.pop()
print(stack1.peek())

