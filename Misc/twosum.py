from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(len(nums)):
            if target - nums[i] in visited:
                return [visited[target - nums[i]], i]
            visited[nums[i]] = i


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(sol.twoSum([3, 2, 4], 6))  # [1, 2]
print(sol.twoSum([3, 3], 6))  # [0, 1]
print(sol.twoSum([3, 2, 3], 6))  # [0, 2]
print(sol.twoSum([3, 2, 4], 6))  # [1, 2]
print(sol.twoSum([3, 2, 4], 6))  # [1, 2]
