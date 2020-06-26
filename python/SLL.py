class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if(self.head == None):
            return -1
        i = 0
        runner = self.head
        while(i < index and runner != None):
            
            i += 1
            runner = runner.next
        if(runner == None):
            return -1
        return runner.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.head = Node(val, self.head)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if(self.head == None):
            self.head = Node(val)
        else: 
            runner = self.head
            while(runner.next != None):
                runner = runner.next
            runner.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if(index == 0):
            self.head = Node(val, self.head)
            return
        i = 0
        runner = self.head
        while(runner != None):
            if((i+1) == index):
                runner.next = Node(val, runner.next)
                return
            i += 1
            runner = runner.next

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if(self.head == None):
            return
        if(index == 0):
            self.head = self.head.next
            return
        i=0
        runner = self.head
        while(runner != None):
            if((i+1) == index and runner.next != None):
                runner.next = runner.next.next
            i += 1
            runner = runner.next
    
    def print(self) -> None:
        runner = self.head
        arr = []
        while(runner != None):
            arr.append(runner.val)
            runner = runner.next
        print(arr)

list1 = SinglyLinkedList()
print(list1.get(0)) # -> -1
list1.deleteAtIndex(2)
list1.addAtIndex(0,7)
list1.addAtHead(2)
list1.addAtHead(1)
list1.print() # -> [1,2,7]
list1.addAtIndex(3,0)
list1.print() # -> [1,2,7,0]
list1.addAtIndex(5,3)
list1.print() # -> [1,2,7,0]
print(list1.get(3)) # -> 0