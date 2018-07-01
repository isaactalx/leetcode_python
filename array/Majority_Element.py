"""
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty
and the majority element always exist in the array.

Input: [2,2,1,1,1,2,2]
Output: 2
"""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major, count = nums[0], 1
        for i in range(1, len(nums)):
            if count == 0:
                major = nums[i]
                count += 1
            elif major == nums[i]:
                count += 1
            else:
                count -= 1
        return major


"""
test
"""
if __name__ == '__main__':
    lists = [2, 2, 1, 1, 1, 2, 2]
    res = Solution().majorityElement(lists)
    assert res == 2
