"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
e.g.:
Input: [7,1,5,3,6,4]
Output: 5

"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_index = max_val = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[min_index]:
                min_index = i
            max_val = max(max_val, prices[i] - prices[min_index])
        return max_val


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
