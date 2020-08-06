"""
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.
Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.
So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
1) Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
2) Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
3) As long as a house is in the heaters' warm radius range, it can be warmed.
4) All the heaters follow your radius standard and the warm radius will the same.
"""

class Solution:
    def findRadius(self, houses: [int], heaters: [int]) -> int:
        houses.sort()
        heaters.sort()
        heaters += [float('inf')]
        r = j = 0
        for house in houses:
            while abs(house - heaters[j]) >= abs(house - heaters[j+1]):
                j += 1
            r = max(r, abs(house - heaters[j]))
        return r

import unittest

class hashSetTest(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test1(self):
        self.assertEqual(self.obj.findRadius([1,2,3], [2]), 1)

    def test2(self):
        self.assertEqual(self.obj.findRadius([1,2,3,4,5], [1,2,3,4,5,3]), 0)

    def test3(self):
        self.assertEqual(self.obj.findRadius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923], 
        [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]), 161834419)

    def test4(self):
        self.assertEqual(self.obj.findRadius([25921153,510616708],
        [771515668,357571490,44788124,927702196,952509530]), 153045218)

    def test5(self):
        self.assertEqual(self.obj.findRadius([35308228,158374933,75260298,824938981,595028635,962408013,137623865,997389814,20739063],
        [635339425,654001669,777724115,269220094,34075629,478446501,864546517]), 132843297)


if __name__ == '__main__':
    unittest.main()