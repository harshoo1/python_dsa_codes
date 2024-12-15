""" STACK """

#1. stack using list
class Stack:
    def __init__(self):
        self.value = []
#2. check if stack is_empty() ?
    def is_empty(self):
        return len(self.value) == 0
#3. push() method for stack
    def push(self,data):
        self.value.append(data)
#4. pop() method for stack
    def pop(self):
        if not self.is_empty():
            return self.value.pop()
        else:
            raise IndexError("Empty Stack")
#5. peek() method for stack
    def peek(self):
        if not self.is_empty():
            return self.value[-1]
        else:
            raise IndexError("Empty Stack")
#6. check size of stack.  size()
    def size(self):
        return len(self.value)



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

# we can't use iterator here to access elements in stack

