# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

# Example:

# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

class Solution:
    def __init__(self):
        self.mem = {}
    def numTrees(self, n: int) -> int:
        if(n == 1 or n == 0):
            return 1
        if(n in self.mem):
            return self.mem[n]
        count = 0
        for i in range(1,n+1):
            count += self.numTrees(i-1) * self.numTrees(n-i)
        self.mem[n] = count
        return self.mem[n]
func = Solution()
print(func.numTrees(3)) # -> 5
print(func.numTrees(5)) # -> 42