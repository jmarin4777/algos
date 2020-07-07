"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""

# **********************************************************************************************************************************************************************************

# class MyStack:
#     def __init__(self):
#         self.stack = []
        
#     def pushToTop(self, x: int) -> None:
#         self.stack.append(x)
        
#     def popFromTop(self) -> int:
#         return self.stack.pop()
    
#     def peekFromTop(self) -> int:
#         return self.stack[len(self.stack)-1]
    
#     def isEmpty(self) -> bool:
#         if len(self.stack) > 0:
#             return False
#         return True

# class MyQueue:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.stack = MyStack()
#         self.queue = self.stack.stack

#     def push(self, x: int) -> None:
#         """
#         Push element x to the back of queue.
#         """
#         self.stack.pushToTop(x)
#         return self

#     def pop(self) -> int:
#         """
#         Removes the element from in front of queue and returns that element.
#         """
#         if len(self.queue) == 1:
#             return self.stack.popFromTop()
#         stack2 = MyStack()
#         while self.queue:
#             stack2.pushToTop(self.stack.popFromTop())
#         temp = stack2.popFromTop()
#         while stack2.stack:
#             self.stack.pushToTop(stack2.popFromTop())
#         return temp

#     def peek(self) -> int:
#         """
#         Get the front element.
#         """
#         if len(self.queue) == 1:
#             return self.stack.peekFromTop()
#         stack2 = MyStack()
#         while self.queue:
#             stack2.pushToTop(self.stack.popFromTop())
#         temp = stack2.peekFromTop()
#         while stack2.stack:
#             self.stack.pushToTop(stack2.popFromTop())
#         return temp

#     def empty(self) -> bool:
#         """
#         Returns whether the queue is empty.
#         """
#         return self.stack.isEmpty()

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.front = None

    def push(self, x: int) -> None:
        if not self.s1:
            self.front = x
        self.s1.append(x)
        return self

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        return self.front

    def empty(self) -> bool:
        if len(self.s1) == 0 and len(self.s2) == 0:
            return True
        return False

import unittest

class queueFromStackTest(unittest.TestCase):
    def setUp(self):
        self.obj = MyQueue()

    def test1(self):
        self.obj.push(1).push(2)
        self.assertEqual(self.obj.peek(), 1)
        self.assertEqual(self.obj.pop(), 1)
        self.assertEqual(self.obj.empty(), False)

    def test2(self):
        self.obj.push(1)
        self.assertEqual(self.obj.pop(), 1)
        self.assertEqual(self.obj.empty(), True)

if __name__ == '__main__':
    unittest.main()