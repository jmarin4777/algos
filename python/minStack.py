"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Constraints:
Methods pop, top and getMin operations will always be called on non-empty stacks.
"""

class MinStack:

    def __init__(self):
        self.stack = []

    # as elements are added, the current min needs to be saved with the element so that if the overall min element gets 
    # removed, the previous min can still be found
    def push(self, x: int) -> None:
        min = self.getMin()
        if min == None or x < min:
            self.stack.append( (x, x) )
        else:
            self.stack.append( (x, min) )
        return self

    def pop(self) -> None:
        self.stack.pop()
        return self

    def top(self) -> int:
        return self.stack[len(self.stack)-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.stack[len(self.stack)-1][1]

import unittest

class minStackTest(unittest.TestCase):
    def setUp(self):
        self.obj = MinStack()

    def test1(self):
        self.obj.push(-2).push(0).push(-3)
        self.assertEqual(self.obj.getMin(), -3)
        self.obj.pop()
        self.assertEqual(self.obj.top(), 0)
        self.assertEqual(self.obj.getMin(), -2)

    def test2(self):
        self.obj.push(0).push(1).push(0)
        self.assertEqual(self.obj.getMin(), 0)
        self.obj.pop()
        self.assertEqual(self.obj.getMin(), 0)

if __name__ == '__main__':
    unittest.main()