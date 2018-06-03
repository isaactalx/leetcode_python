"""
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).
Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.
Input:
bits = [1, 1, 1, 0]
Output: False
"""


class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i, N = 0, len(bits) - 1
        while i < N:
            i += bits[i] + 1
        return i == N


print(Solution().isOneBitCharacter([1, 1, 1, 0]))
