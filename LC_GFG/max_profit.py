from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 10**4
        profit = 0

        for price in prices:
            if price < buy:  # update buy
                buy = price
            else:  # when we have a min buy, we should calculate profit
                profit = max(profit, price - buy)

        return profit


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
