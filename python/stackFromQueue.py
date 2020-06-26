# Implement the following operations of a stack using queues.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.

# Example:

# MyStack stack = new MyStack();

# stack.push(1);
# stack.push(2);  
# stack.top();   // returns 2
# stack.pop();   // returns 2
# stack.empty(); // returns false
# Notes:

# You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)
        return self

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        length = len(self.q1)
        if length == 0:
            return None
        q2 = deque()
        for i in range(length):
            if i == length-1:
                temp = self.q1.popleft()
                self.q1 = q2
                return temp
            q2.append(self.q1.popleft())

    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.q1) > 0:
            return self.q1[len(self.q1)-1]
        return None

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.q1) > 0:
            return False
        return True

stack = MyStack()

stack.push(1)
stack.push(2)
print(stack.top())      # returns 2
print(stack.pop())      # returns 2
print(stack.empty())    # returns false
