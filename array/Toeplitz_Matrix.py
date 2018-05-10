"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: True
Example 2:
Input: matrix = [[1,2],[2,2]]
Output: False

Note:
matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].
"""


class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all(r == 0 or c == 0 or matrix[r - 1][c - 1] == val
                   for r, row in enumerate(matrix) for c, val in
                   enumerate(row))  # just judge if all r[i-1][j-1]==r[i][j]


"""
test
"""
if __name__ == '__main__':
    matrix_1 = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    res = Solution().isToeplitzMatrix(matrix_1)
    assert res == True
