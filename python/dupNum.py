# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

# Example 1:
# Input: [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: [3,1,3,4,2]
# Output: 3

# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.

list1 = [1,3,4,2,2]
class Solution:
    #space complexity O(n) as the max length of set will be len(nums)-1
    def findDuplicate1(self, nums: [int]) -> int:
        nums2 = set()
        for i in nums:
            if i in nums2:
                return i
            nums2.add(i)

    #really slow for loop + in operation + slicing O(n^3)?
    def findDuplicate2(self, nums: [int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] in nums[0:i] + nums[i+1:len(nums)]:
                return nums[i]

    #tortoise and hare approach, first while loop finds intersection within loop, second finds start of loop (dup)
    #time O(n), extra space O(1)
    def findDuplicate3(self, nums: [int]) -> int:
        runner1 = runner2 = nums[0]
        while True:
            runner1 = nums[runner1]
            runner2 = nums[nums[runner2]]
            if runner1 == runner2:
                break

        runner1 = nums[0]
        while runner1 != runner2:
            runner1 = nums[runner1]
            runner2 = nums[runner2]
        return runner2
f = Solution()
print(f.findDuplicate1(list1))
print(f.findDuplicate2(list1))
print(f.findDuplicate3(list1))