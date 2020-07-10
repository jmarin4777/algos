"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

#    Example:
#        7
#      /   \
#    3       15
#          /   \
#        9       20


obj = BSTIterator(root)
obj.next()        # return 3
obj.next()        # return 7
obj.hasNext()     # return true
obj.next()        # return 9
obj.hasNext()     # return true
obj.next()        # return 15
obj.hasNext()     # return true
obj.next()        # return 20
obj.hasNext()     # return false

Note:
next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.leftTraversal(root)
        
    # before returning the node value, next will first check if there is a right child attached, and if so, it will run left traversal to add each node to the call stack in order.
    def next(self) -> int:
        """
        @return the next smallest number
        """
        root = self.stack.pop()
        if root.right:
            self.leftTraversal(root.right)
        return root.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.stack:
            return True
        return False
        
    # creates a call stack for the next method with the last appended node being the minimum since it is the furthest left
    def leftTraversal(self, root: TreeNode) -> None:
        while root:
            self.stack.append(root)
            root = root.left        
