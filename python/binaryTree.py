class TreeNode:
    def __init__(self, val):
        self.left = self.right = None
        self.val = val

class BinaryTree:
    def __init__(self):
        self.root = None
        self.count = 0

    #for a given array, to construct in level order fashion (from starting at the root moving from left to right at each level)
    #the child nodes for each index i are 2*i+1 (left child) and 2*i+2 (right child)
    def createLevelOrder(self, arr, i=None, n=None):
        if i == None:
            i = 0
        if n == None: 
            n = len(arr)
        if i < n:
            root = TreeNode(arr[i])
            if(2*i+1 < n):
                root.left = self.createLevelOrder(arr, 2*i+1, n)
            if(2*i+2 < n):
                root.right = self.createLevelOrder(arr, 2*i+2, n)
        return root

    #creating a list from a BST
    def BSTtoList(self, root):
        if root == None:
            return []
        return self.BSTtoList(root.left) + [root.val] + self.BSTtoList(root.right)

    #coverting a sorted linked list first to an array list and then to a BST
    def sortedListToBST(self, listNode) -> TreeNode:
        runner = listNode
        arr = []
        while runner != None:
            arr.append(runner.val)
            runner = runner.next
        return self.createFromMedian(arr, int((len(arr)-1)/2))

    #using the median in order to create a height balanced BST from a list
    def createFromMedian(self, arr, i):
        if len(arr) == 0:
            return None
        root = TreeNode(arr[i])
        if(len(arr) == 3):
            root.left = TreeNode(arr[0])
            root.right = TreeNode(arr[2])
            return root
        
        left = arr[0:i]
        if(len(left) > 0):
            root.left = self.createFromMedian(left, int((len(left)-1)/2))
        right = arr[i+1:len(arr)]
        if(len(right) >0):
            root.right = self.createFromMedian(right, int((len(right)-1)/2))
        return root

    def countNodes(self, root):
        if root == None:
            return self.count
        self.count += 1
        self.countNodes(root.left)
        self.countNodes(root.right)
        return self.count

list1 = [-10,-3,0,2,5,9]
tree1 = BinaryTree()
tree1.root = tree1.createFromMedian(list1, int((len(list1)-1)/2))
print(tree1.countNodes(tree1.root))
print(tree1.BSTtoList(tree1.root))

list2 = [1,2,3,4,5,6]
tree2 = BinaryTree()
tree2.root = tree2.createLevelOrder(list2)
print(tree2.countNodes(tree2.root))
print(tree2.BSTtoList(tree2.root))