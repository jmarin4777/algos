"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network 
connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure 
that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def BSTToList(root):
            if root is None:
                return []
            return [str(root.val)] + BSTToList(root.left) + BSTToList(root.right)
        
        l = BSTToList(root)
        if l:
            return ",".join(l)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        # str should be root values separated by commas
        if not data:
            return
        q = deque(data.split(','))
        
        def queueToBST(min, max):
            next = int(q[0])
            if next >= min and next <=max:
                root = TreeNode(int(q.popleft()))
            else:
                return None
            if q:
                root.left = queueToBST(min, root.val)
            if q:
                root.right = queueToBST(root.val, max)
            return root
        return queueToBST(float('-inf'), float('inf'))

root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)
codec = Codec()
strBST = codec.serialize(root)
print(strBST) # -> "7,3,15,9,20"
print(codec.deserialize(strBST)) # -> root(7)
