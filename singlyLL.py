"""  SINGLY LINKED LIST"""

#1. define a class Node to describe a node of a singly linked list

class Node:
    def __init__(self, val = None , next = None):
        self.val = val
        self.next = next

#2. singly linked list class

class SinglyLL:
    def __init__(self, start = None):
        self.start = start
    #3. check that if class is empty ?
    def isEmpty(self):
        return self.start == None
    #4. method to insert data at start
    def insertAtStart(self,data):
        n = Node(val=data,next=self.start)
        self.start = n  
    #5. insert at last
    def insertAtLast(self,data):
        n = Node(val=data)
        if not self.isEmpty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n
    #6. search for value in the singly LL
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.val == data:
                return temp
            temp = temp.next
        return None
    #7. insert after some node/in between sll
    def insertAfter(self,temp,data):
        if temp is not None:
            n = Node(data,temp.next)
            temp.next = n
    #8. print all element of list
    def printSll(self):
        temp = self.start
        while temp is not None:
            print(temp.val,end=' ')
            temp = temp.next
    #9. delete first node
    def deleteFirstNode(self):
        if self.start is not None:
            self.start = self.start.next
    #10. delete last element
    def deleteLastNode(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
                temp.next = None
    #11. delete some random element
    def deleteRandomNode(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.val == data:
                self.start = None
            else:
                temp = self.start
                if temp.val ==data:
                    self.start = temp.next
                else:
                    while temp.next is not None:
                        if temp.next.val == data:
                            temp.next = temp.next.next
                            break
                        temp = temp.next
# function to access the slliterator 
    def __iter__(self):
        return slliterator(self.start)
    
# making an iterator for printing the sll
class slliterator:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.val
        self.current =  self.current.next
        return data



#main code
mySinglyLL = SinglyLL()
mySinglyLL.insertAtStart(20)
mySinglyLL.insertAtLast(30)
mySinglyLL.insertAfter(mySinglyLL.search(20),40)





mySinglyLL.printSll()
mySinglyLL.deleteRandomNode(40)
print("result after deleting some elemnt")

# loop for iterating and printing value of sll
for x in mySinglyLL:
    print(x,end=' ')


    




            