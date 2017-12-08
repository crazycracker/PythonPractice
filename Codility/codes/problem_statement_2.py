class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, initdata):
        self.data = initdata

    def setNext(self, newnext):
        self.next = newnext


class LinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.getNext()
        return count


myList = LinkedList()
print("Enter the number of elements to be entered \n")
count = int(input())
print("Enter the elements")
for i in range(count):
    number = int(input())
    myList.add(number)
print("The size of the list is %d" % myList.size())
