# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,3,2]
# Output: 3
# Example 2:

# Input: [0,1,0,1,0,1,99]
# Output: 99

class Solution:
    def singleNumber(self, nums) -> int:
        lib = {}
        for i in range(len(nums)):
            if nums[i] in lib:
                lib[nums[i]] += 1
                if lib[nums[i]] == 3:
                    del lib[nums[i]]
            else:
                lib[nums[i]] = 1
        return next(iter(lib))

func = Solution()
print(func.singleNumber([2,2,3,2]))
