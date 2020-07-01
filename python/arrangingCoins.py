from collections import defaultdict

class Solution:
    #takes too long for large integers, O(n) time complexity
    def arrangeCoins1(self, n: int) -> int:
        lib = defaultdict(int)
        i = 1
        count = 0
        while n > 0:
            if lib[i] < i:
                lib[i] += 1
                n -= 1
            if lib[i] == i:
                count += 1
                i+=1
        return count

    """
    the area of a square made from k rows of coins would be k^2, but the area of the actual staircase is more than half 
    this.  Adding one to the length, k(k+1)/2 now gives us the area of the staircase which is the total number of coins 
    if the rows are completely full.  Ex: n=10 coins, 4 rows -> 4(4+1)/2 = 10
    we know that the number of rows must be between 0 - n so we can search starting at the middle (0+n)/2 
    O(log n) time complexity
    """
    def arrangeCoins2(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (left + right)//2
            check = k*(k+1)/2
            if check == n:
                return k
            if check < n:
                left = k+1
            else:
                right = k-1
        return right

import unittest

class arrangeCoinsTest(unittest.TestCase):
    def setUp(self):
        self.f = Solution()

    def testCoins1(self):
        self.assertEqual(self.f.arrangeCoins1(1), 1)
        self.assertEqual(self.f.arrangeCoins1(8), 3)
        self.assertEqual(self.f.arrangeCoins1(0), 0)
        self.assertEqual(self.f.arrangeCoins1(2), 1)
        self.assertEqual(self.f.arrangeCoins1(15), 5)

    def testCoins2(self):
        self.assertEqual(self.f.arrangeCoins2(1), 1)
        self.assertEqual(self.f.arrangeCoins2(8), 3)
        self.assertEqual(self.f.arrangeCoins2(0), 0)
        self.assertEqual(self.f.arrangeCoins2(2), 1)
        self.assertEqual(self.f.arrangeCoins2(15), 5)

if __name__ == '__main__':
    unittest.main()