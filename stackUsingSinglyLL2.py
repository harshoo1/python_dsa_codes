""" stack using inheriting the linked list class 
singly ll as parent class and stack as child class"""

from sll_package.sll_class import *
 
 #1. defining stack class
class Stack:
    def __init__(self):
        self.mylist = SinglyLL()
#2. is_empty() ?
    def is_empty(self):
        self.mylist.isEmpty()
#3. push data
    def push(self,data):
        self.mylist.insertAtStart()
#4. pop data        
   


