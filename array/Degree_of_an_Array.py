"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Input: [1,2,2,3,1,4,2]
Output: 6
"""
import collections


class Solution:
    def findShortestSubArray(self, nums):
        first, last = {}, {}
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            last[v] = i
        c = collections.Counter(nums)
        degree = max(c.values())
        return min(last[v] - first[v] + 1 for v in c if c[v] == degree)


"""
test
"""
if __name__ == '__main__':
    lists = [1, 2, 2, 3, 1, 4, 2]
    res = Solution().findShortestSubArray(lists)
    assert res
