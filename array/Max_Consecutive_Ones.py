"""
Given a binary array, find the maximum number of consecutive 1s in this array.
Input: [1,1,0,1,1,1]
Output: 3
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        strs = "".join(map(str, nums)).split('0')
        return max(map(len, strs))


print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
