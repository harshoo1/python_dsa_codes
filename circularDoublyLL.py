class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class CircularDoublyLL:
    def __init__(self):
        self.start = None

    def insertAtStart(self, data):
        n = Node(val=data)
        if self.start is None:
            self.start = n
            n.next = n
            n.prev = n
        else:
            last = self.start.prev
            n.next = self.start
            n.prev = last
            self.start.prev = n
            last.next = n
            self.start = n

    def insertAtLast(self, data):
        n = Node(val=data)
        if self.start is None:
            self.start = n
            n.next = n
            n.prev = n
        else:
            last = self.start.prev
            last.next = n
            n.prev = last
            n.next = self.start
            self.start.prev = n

    def search(self, data):
        if self.start is None:
            return None
        temp = self.start
        while True:
            if temp.val == data:
                return temp
            temp = temp.next
            if temp == self.start:
                break
        return None

    def insertAfter(self, temp, data):
        if temp is not None:
            n = Node(val=data, next=temp.next, prev=temp)
            temp.next.prev = n
            temp.next = n

    def printDll(self):
        if self.start is None:
            return
        temp = self.start
        while True:
            print(temp.val, end=' ')
            temp = temp.next
            if temp == self.start:
                break

    def deleteFirstNode(self):
        if self.start is None:
            return
        if self.start.next == self.start:
            self.start = None
        else:
            last = self.start.prev
            self.start = self.start.next
            self.start.prev = last
            last.next = self.start

    def deleteLastNode(self):
        if self.start is None:
            return
        if self.start.next == self.start:
            self.start = None
        else:
            last = self.start.prev
            second_last = last.prev
            second_last.next = self.start
            self.start.prev = second_last

    def deleteRandomNode(self, data):
        if self.start is None:
            return
        temp = self.start
        while True:
            if temp.val == data:
                if temp.next == temp:  # Only one node
                    self.start = None
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    if temp == self.start:
                        self.start = temp.next
                break
            temp = temp.next
            if temp == self.start:
                break

    def __iter__(self):
        return cdlliterator(self.start)

class cdlliterator:
    def __init__(self, start):
        self.start = start
        self.current = start
        self.first_pass = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None or (self.current == self.start and not self.first_pass):
            raise StopIteration
        data = self.current.val
        self.current = self.current.next
        self.first_pass = False
        return data

# Main Code
myCircularDoublyLL = CircularDoublyLL()
myCircularDoublyLL.insertAtStart(20)
myCircularDoublyLL.insertAtLast(30)
myCircularDoublyLL.insertAfter(myCircularDoublyLL.search(20), 40)

myCircularDoublyLL.printDll()
print("\nResult after deleting an element:")
myCircularDoublyLL.deleteRandomNode(40)

for x in myCircularDoublyLL:
    print(x, end=' ')
