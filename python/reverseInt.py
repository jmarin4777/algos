"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1
        reverse = int(str(abs(x))[::-1])
        if sign * reverse < 2 ** 31 and sign * reverse >= -(2 ** 31):
            return sign * reverse
        else:
            return 0

obj = Solution()
print(obj.reverse(123)) # -> 321
print(obj.reverse(-123)) # -> -321
print(obj.reverse(120)) # -> 21
print(obj.reverse(1534236469)) # -> 0
print(obj.reverse(-2147483648)) # -> 0
print(obj.reverse(2147483647)) # -> 0