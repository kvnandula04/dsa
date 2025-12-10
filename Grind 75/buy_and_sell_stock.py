from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # Expected Output: 5
print(sol.maxProfit([2, 1, 4]))  # Expected Output: 3
