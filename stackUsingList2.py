""" Stack using list 2
extending list class to implement stack """

#1. inheriting list class to make stack |  stack as child class and list as the  parent class
class Stack(list):
#2. is_empty()
    def is_empty(self):
        return len(self) ==0
#3. push()
    def push(self,data):
        self.append(data)
#4. pop()
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("stack is empty")
#5. peek()
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("stack empty")
#6. size()
    def size(self):
        return len(self)

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



