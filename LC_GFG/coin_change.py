from typing import List


class Solution:
    def coinChange(coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if amount - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] != float("inf") else -1


sol = Solution
ans = sol.coinChange([1, 2, 5], 11)
print(ans)
