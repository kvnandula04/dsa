from typing import List


# Code
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Method 1
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in nums[i + 1 :]:
        #         return [i, nums.index(diff, i + 1)]

        # Method 2
        # visited = {}

        # for i in range(len(nums)):
        #     visited[nums[i]] = i
        # for i in range(len(visited)):
        #     diff = target - nums[i]
        #     if diff in visited and visited[diff] != i:
        #         return [i, visited[diff]]

        # Method 3
        visited = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in visited:
                return [i, visited[diff]]

            visited[nums[i]] = i
        return []


# Test
sol = Solution()

solution = sol.twoSum([3, 2, 4], 6)
print(solution)  # Expected Output: [1, 2]
solution = sol.twoSum([2, 7, 11, 15], 9)
print(solution)  # Expected Output: [0, 1]
solution = sol.twoSum([3, 3], 6)
print(solution)  # Expected Output: [0, 1]
