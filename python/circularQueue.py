"""
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle 
and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next 
element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.

Note:
All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Queue library.
"""

class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value=value
        self.next=next
        self.prev=prev

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.front = self.rear = None
        self.maxSize = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.size == self.maxSize:
            return False
        elif self.size == 0:
            self.front, self.rear = Node(value), Node(value)
            self.front.next = self.front.prev = self.rear
            self.rear.next = self.rear.prev = self.front
        elif self.size == 1:
            self.rear = Node(value, self.front, self.front)
            self.front.next = self.front.prev = self.rear
        else:
            temp = self.rear
            self.rear = Node(value, self.front, self.rear)
            self.front.prev = temp.next = self.rear
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.size == 0:
            return False
        self.front = self.front.next
        self.rear.next, self.front.prev = self.front, self.rear
        self.size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.size > 0:
            return self.front.value
        return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.size > 0:
            return self.rear.value
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self.size == self.maxSize:
            return True
        return False


obj = MyCircularQueue(4)                      # set the size to be 3
print(obj.enQueue(1))                         # return true
print(obj.enQueue(2))                         # return true
print(obj.enQueue(3))                         # return true
print(obj.enQueue(4))                         # return true
print(obj.enQueue(5))                         # return false, the queue is full
print(obj.Rear())                             # return 4
print(obj.isFull())                           # return true
print(obj.deQueue())                          # return true
print(obj.enQueue(5))                         # return true
print(obj.Rear())                             # return 4