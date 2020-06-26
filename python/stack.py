class StackNode:
    def __init__(self, value=None, next=None):
        self.val = value
        self.next = next

class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.front = StackNode(x, self.front)
        return self

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.front == None:
            return None
        temp = self.front.val
        self.front = self.front.next
        return temp

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.front.val

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.front == None:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()