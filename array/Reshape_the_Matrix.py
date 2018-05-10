"""
You're given a matrix represented by a two-dimensional array, and two positive integers r and c
representing the row number and column number of the wanted reshaped matrix, respectively.
The reshaped matrix need to be filled with all the elements of the original matrix
in the same row-traversing order as they were.
If the 'reshape' operation with given parameters is possible and legal,
output the new reshaped matrix; Otherwise, output the original matrix.
Input:
nums =
[[1,2],[3,4]] r = 1, c = 4
Output:
[[1,2,3,4]]
Input:
nums = [[1,2],[3,4]] r = 2, c = 4
Output:
[[1,2],[3,4]]
"""


class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
            return nums
        num_new = [x for row in nums for x in row]
        return [num_new[i:i + c] for i in range(0, len(num_new), c)]


"""
test
"""
if __name__ == '__main__':
    nums = [[1, 2], [3, 4]]
    r, c = 1, 4
    res = Solution().matrixReshape(nums, r, c)
    assert res == [[1, 2, 3, 4]]
