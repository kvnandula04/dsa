from typing import List
import math


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = nums[0]
        current_sum = nums[0]
        p = 1  # start from 1 to prevent double count

        while p < len(nums):
            if current_sum > 0:
                current_sum += nums[p]  # extend subarray
            else:
                current_sum = nums[p]  # start fresh

            best_sum = max(best_sum, current_sum)
            p += 1

        return best_sum


sol = Solution()

print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(sol.maxSubArray([1]))
print(sol.maxSubArray([5, 4, -1, 7, 8]))
