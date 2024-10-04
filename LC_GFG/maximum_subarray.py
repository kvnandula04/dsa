from typing import List


# Implement using Kadane's algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]

        for num in nums[1:]:
            # Pick max between current number and subarray until current number
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum


sol = Solution()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(sol.maxSubArray([1]))  # 1
print(sol.maxSubArray([-1]))  # -1
print(sol.maxSubArray([-2, -1]))  # -1
