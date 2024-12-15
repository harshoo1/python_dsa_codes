"""queue using list"""


#1. defint class
class Queue:
    def __init__(self):
        self.value= []
        self.front = None
        self.rare = None        
#2. is_empty()
    def is_empty(self):
        return len(self.value) is None
#3. enqueue() 
    def enqueue(self,data):
        self.value.append(data)
#4. dequeue()
    def dequeue(self):
        if not self.is_empty():
            self.value.pop(0)
        else:
            raise IndexError("underflow")
#5. get_front()
    def get_front(self):
        if not self.is_empty():
            return self.value[0]
        else: 
            raise IndexError("underflow")
#6. get_rear()
    def get_rear(self):
        if not self.is_empty():
            return self.value[-1]
        else:
            raise IndexError("underflow")
#7. size()
    def size(self):
        return len(self.value)

#main code

q = Queue()
#q.enqueue(15)
#q.enqueue(20)
#q.enqueue(30)
#q.enqueue(50)
#print(q.get_front())
try:
    print(q.get_front())
except IndexError as e:
    print(e.args[0])
