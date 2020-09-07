"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) 
and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""

class Solution:
    #brute force, time complexity (O(n^2))
    def maxArea1(self, height: [int]) -> int:
        a = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                temp = min(height[i], height[j]) * (j-i)
                if temp > a:
                    a = temp
        return a

    #two pointers, time complexity (O(n))
    def maxArea2(self, height: [int]) -> int:
        a = l = 0
        r = len(height) - 1
        while (l<r):
            a = max(a, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -=1
        return a

import unittest

class hashSetTest(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test1(self):
        self.assertEqual(self.obj.maxArea1([1,8,6,2,5,4,8,3,7]), 49)

    def test2(self):
        self.assertEqual(self.obj.maxArea2([1,8,6,2,5,4,8,3,7]), 49)

if __name__ == '__main__':
    unittest.main()