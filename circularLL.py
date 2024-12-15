class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class CircularLL:
    def __init__(self):
        self.start = None

    def insertAtStart(self, data):
        new_node = Node(val=data)
        if self.start is None:
            self.start = new_node
            new_node.next = new_node
        else:
            temp = self.start
            while temp.next != self.start:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.start
            self.start = new_node

    def insertAtLast(self, data):
        new_node = Node(val=data)
        if self.start is None:
            self.start = new_node
            new_node.next = new_node
        else:
            temp = self.start
            while temp.next != self.start:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.start

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

    def insertAfter(self, node, data):
        if node is not None:
            new_node = Node(val=data, next=node.next)
            node.next = new_node

    def printList(self):
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
            temp = self.start
            while temp.next != self.start:
                temp = temp.next
            temp.next = self.start.next
            self.start = self.start.next

    def deleteLastNode(self):
        if self.start is None:
            return
        if self.start.next == self.start:
            self.start = None
        else:
            temp = self.start
            while temp.next.next != self.start:
                temp = temp.next
            temp.next = self.start

    def deleteRandomNode(self, data):
        if self.start is None:
            return
        if self.start.val == data and self.start.next == self.start:
            self.start = None
            return
        temp = self.start
        prev = None
        while True:
            if temp.val == data:
                if prev is not None:
                    prev.next = temp.next
                else:
                    last = self.start
                    while last.next != self.start:
                        last = last.next
                    last.next = temp.next
                    self.start = temp.next
                break
            prev = temp
            temp = temp.next
            if temp == self.start:
                break

    def __iter__(self):
        return CircularLLIterator(self.start)

class CircularLLIterator:
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
myCircularLL = CircularLL()
myCircularLL.insertAtStart(20)
myCircularLL.insertAtLast(30)
myCircularLL.insertAfter(myCircularLL.search(20), 40)

myCircularLL.printList()
print("\nResult after deleting an element:")
myCircularLL.deleteRandomNode(40)

for x in myCircularLL:
    print(x, end=' ')
