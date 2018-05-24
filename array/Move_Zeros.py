"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i, num in enumerate(nums):
            if num:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
        return nums


print(Solution().moveZeroes([0, 1, 0, 2, 12]))
