"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice
in the array, and it should return false if every element is distinct.
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums)-len(set(nums))>0

"""
test
"""
if __name__ == '__main__':
    lists = [2, 2, 1, 1, 1, 2, 2]
    res = Solution().containsDuplicate(lists)
    assert res