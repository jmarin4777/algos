"""
Design a stack which supports the following operations.

Implement the CustomStack class:

- CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack or do nothing if the stack reached the maxSize.
- void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
- int pop() Pops and returns the top of stack or -1 if the stack is empty.
- void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.

Constraints:

1 <= maxSize <= 1000
1 <= x <= 1000
1 <= k <= 1000
0 <= val <= 100
At most 1000 calls will be made to each method of increment, push and pop each separately.
"""

# stack implementing a linked list

# class StackNode:
#     def __init__(self, value=None, next=None):
#         self.val = value
#         self.next = next

# class CustomStack:
#     def __init__(self, maxSize: int):
#         self.top = None
#         self.maxSize = maxSize
#         self.count = 0

#     def push(self, x: int) -> None:
#         if self.count < self.maxSize:
#             if self.top == None:
#                 self.top = StackNode(x)
#             else:
#                 self.top = StackNode(x, self.top)
#             self.count += 1

#     def pop(self) -> int:
#         if self.top == None:
#             return -1
#         temp = self.top.val
#         self.top = self.top.next
#         self.count -= 1
#         return temp

#     def increment(self, k: int, val: int) -> None:
#         if k < self.count:
#             start = self.count - k
#         else:
#             start = 0
#         i = 0
#         runner = self.top
#         while runner != None:
#             if i >= start:
#                 runner.val += val
#             i += 1
#             runner = runner.next

# **************************************************************************************************************************************************************************************
# stack implementing an array list

# class CustomStack:
#     def __init__(self, maxSize: int):
#         self.maxSize = maxSize
#         self.stack = []

#     def push(self, x: int) -> None:
#         if len(self.stack) < self.maxSize:
#             self.stack.append(x)

#     def pop(self) -> int:
#         return self.stack.pop()

#     def increment(self, k: int, val: int) -> None:
#         self.stack[len(self.stack) - k:len(self.stack)] += val

# **************************************************************************************************************************************************************************************
# stack implementing an array list with an additional array list to keep track of increments
# with index i, an increment at inc[i] will be applied to all values from stack[0] to stack[i]
# when a value is popped, the increment must also be moved from inc[i] to inc[i-1]

class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        if len(self.stack) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            self.inc[min(k,len(self.stack))-1] += val

obj = CustomStack(3)                 # Stack is Empty []
obj.push(1)                          # stack becomes [1]
obj.push(2)                          # stack becomes [1, 2]
obj.pop()                            # return 2 --> Return top of the stack 2, stack becomes [1]
obj.push(2)                          # stack becomes [1, 2]
obj.push(3)                          # stack becomes [1, 2, 3]
obj.push(4)                          # stack still [1, 2, 3], Don't add another elements as size is 4
obj.increment(5, 100)                # stack becomes [101, 102, 103]
obj.increment(2, 100)                # stack becomes [201, 202, 103]
obj.pop()                            # return 103 --> Return top of the stack 103, stack becomes [201, 202]
obj.pop()                            # return 202 --> Return top of the stack 102, stack becomes [201]
obj.pop()                            # return 201 --> Return top of the stack 101, stack becomes []
obj.pop()                            # return -1 --> Stack is empty return -1.