from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            # left portion
            if nums[left] <= nums[mid]:
                if target > nums[mid] or nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1
            # right portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
