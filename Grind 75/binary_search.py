from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            midpoint = (high + low) // 2

            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                low = midpoint + 1
            else:
                high = midpoint - 1

        return -1
