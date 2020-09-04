class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        # r is the reverted number
        r = 0
        # comparing both halves of the original number, we are halfway through when x == r (even number 1221, x == r == 12)
        # or when r > x (odd number 12321, x = 12, r = 123) so the loop only needs to run while x > r
        while x > r:
            # take the modulus of x to get the last digit (121, x % 10 = 1) and add it to the reverted number
            r = r*10 + x % 10
            x = x // 10
        # in the case of an odd number, the last digit can be ignored bc it will still be a palindrome if both sides match
        # Ex: for 12321, x = 12, r = 123, x == r // 10 (3 is ignored as it is in the middle)
        return x == r or x == r // 10

import unittest

class hashSetTest(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    #Negative numbers should return false
    def test1(self):
        self.assertEqual(self.obj.isPalindrome(-121), False)

    #Any number that ends in a zero cannot be a palindrome (Ex: 110 backwards 011) except for 0
    def test2(self):
        self.assertEqual(self.obj.isPalindrome(10), False)
        self.assertEqual(self.obj.isPalindrome(110), False)
        self.assertEqual(self.obj.isPalindrome(0), True)

    #Palindrome numbers should return True
    def test3(self):
        self.assertEqual(self.obj.isPalindrome(121), True)
        self.assertEqual(self.obj.isPalindrome(12321), True)

if __name__ == '__main__':
    unittest.main()