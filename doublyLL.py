class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLL:
    def __init__(self, start=None):
        self.start = start

    def insertAtStart(self, data):
        n = Node(val=data, next=self.start)
        if self.start is not None:
            self.start.prev = n
        self.start = n

    def insertAtLast(self, data):
        n = Node(val=data)
        if self.start is not None:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
            n.prev = temp
        else:
            self.start = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.val == data:
                return temp
            temp = temp.next
        return None

    def insertAfter(self, temp, data):
        if temp is not None:
            n = Node(val=data, next=temp.next, prev=temp)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n

    def printDll(self):
        temp = self.start
        while temp is not None:
            print(temp.val, end=' ')
            temp = temp.next

    def deleteFirstNode(self):
        if self.start is not None:
            if self.start.next is not None:
                self.start = self.start.next
                self.start.prev = None
            else:
                self.start = None

    def deleteLastNode(self):
        if self.start is None:
            return
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def deleteRandomNode(self, data):
        temp = self.start
        while temp is not None:
            if temp.val == data:
                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.start = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
                break
            temp = temp.next

    def __iter__(self):
        return dlliterator(self.start)

class dlliterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.val
        self.current = self.current.next
        return data

# Main Code
myDoublyLL = DoublyLL()
myDoublyLL.insertAtStart(20)
myDoublyLL.insertAtLast(30)
myDoublyLL.insertAfter(myDoublyLL.search(20), 40)

myDoublyLL.printDll()
print("\nResult after deleting an element:")
myDoublyLL.deleteRandomNode(40)

for x in myDoublyLL:
    print(x, end=' ')
