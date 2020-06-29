# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).  The robot can only 
# move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.
# How many possible unique paths are there?

# Example 1:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right

# Example 2:

# Input: m = 7, n = 3
# Output: 28

# Constraints:

# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

class Solution:
    #m = col, n = row
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 0:
            return 0
        
        #storing coordinates (x,y) or (col, row) = number of possible paths. when at the end position, possible paths = 1
        lib = {(m-1, n-1):1}
        
        #iterate through grid starting at end
        for row in range(n-1,-1,-1):
            for col in range(m-1,-1,-1):
                #skip if at end
                if col == m-1 and row == n-1:
                    continue
                right = down = 0
                #checks for path on the right
                if (col+1,row) in lib:
                    right = lib[(col+1,row)]
                #checks for path below
                if (col,row+1) in lib:
                    down = lib[(col,row+1)]
                #sums possible paths
                lib[(col,row)] = right + down
        return lib[0,0]