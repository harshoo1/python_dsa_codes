""" Stack using singly linked list"""

#1. define class
class Node:
    def __init__(self,value = None, next = None):
        self.value = value
        self.next  = next
class Stack:
    def __init__(self):
        self.start = None
        self.value_count = 0    
#2. is_empty()
    def is_empty(self):
        return self.start is None
#3. push()
    def push(self,data):
        n = Node(data,self.start)
        self.start = n
        self.value_count += 1
#4. pop()
    def pop(self):
        if not self.is_empty():
            data = self.start.value
            self.start = self.start.next
            self.value_count -= 1 
            return data
        else:
            raise IndexError("underflow")
#5. peek()
    def peek(self):
        if not self.is_empty():
            return self.start.value
        else:
            raise IndexError("Stack is empty")
#6. size()
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