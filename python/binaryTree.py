class TreeNode:
    def __init__(self, val):
        self.left = self.right = None
        self.val = val


class BinaryTree:
    def __init__(self):
        self.root = None

    #assuming a sorted array with positive integers
    def createFromList(self, arr, i=None, n=None):
        if i == None:
            i = 0
        if n == None: 
            n = 0
        if i < n:
            root = TreeNode(arr[i])
            if(2*i+1 < n):
                root.left = self.createFromList(arr, 2*i+1, n)
            if(2*i+2 < n):
                root.right = self.createFromList(arr, 2*i+2, n)
        return root
    
    def toList(self, root):
        if root == None:
            return []
        return self.toList(root.left) + [root.val] + self.toList(root.right)

    def sortedListToBST(self, listNode) -> TreeNode:
        runner = listNode
        arr = []
        while runner != None:
            arr.append(runner.val)
            runner = runner.next
        return self.createFromSLL(arr, int((len(arr)-1)/2))
        
    def createFromSLL(self, arr, i):
        if len(arr) == 0:
            return None
        root = TreeNode(arr[i])
        if(len(arr) == 3):
            root.left = TreeNode(arr[0])
            root.right = TreeNode(arr[2])
            return root
        
        left = arr[0:i]
        if(len(left) > 0):
            root.left = self.createFromSLL(left, int((len(left)-1)/2))
        right = arr[i+1:len(arr)]
        if(len(right) >0):
            root.right = self.createFromSLL(right, int((len(right)-1)/2))
        return root


list1 = [-10,-3,0,2,5,9]
BST = BinaryTree()
BST.createFromSLL(list1, int((len(list1)-1)/2))