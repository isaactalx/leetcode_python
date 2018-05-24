"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Input:
[4,3,2,7,8,2,3,1]
Output:
[5,6]
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1, len(nums) + 1)).difference(set(nums)))


print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
