class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class SinglyLL:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        return self.start == None

    def insertAtStart(self, data):
        n = Node(val=data, next=self.start)
        self.start = n  

    def insertAtLast(self, data):
        n = Node(val=data)
        if not self.isEmpty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
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
            n = Node(data, temp.next)
            temp.next = n

    def printSll(self):
        temp = self.start
        while temp is not None:
            print(temp.val, end=' ')
            temp = temp.next

    def deleteFirstNode(self):
        if self.start is not None:
            self.start = self.start.next

    def deleteLastNode(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def deleteRandomNode(self, data):
        if self.start is None:
            return
        if self.start.val == data:
            self.start = self.start.next
        else:
            temp = self.start
            while temp.next is not None:
                if temp.next.val == data:
                    temp.next = temp.next.next
                    return
                temp = temp.next

    # def __iter__(self):
    #     return slliterator(self.start)

# class slliterator:
#     def __init__(self, start):
#         self.current = start

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if not self.current:
#             raise StopIteration
#         data = self.current.val
#         self.current = self.current.next
#         return data

