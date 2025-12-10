from typing import List
import itertools


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == sorted(nums, reverse=True):  # if the list is in descending order
            nums.sort()  # rearrange to the smallest permutation
            return nums

        # Step 1: Find the first decreasing element from the right
        decreasing_index = -1
        for i in range(len(nums) - 2, -1, -1):  # Start from second-to-last element
            if nums[i] < nums[i + 1]:
                decreasing_index = i
                break

        # Step 2: Find the smallest element to the right of decreasing_index that's larger than nums[decreasing_index]
        for j in range(len(nums) - 1, decreasing_index, -1):
            if nums[j] > nums[decreasing_index]:
                # Step 3: Swap the elements
                nums[decreasing_index], nums[j] = nums[j], nums[decreasing_index]
                break

        # Step 4: Reverse the elements to the right of decreasing_index
        nums[decreasing_index + 1 :] = reversed(nums[decreasing_index + 1 :])

        return nums


sol = Solution()
print(sol.nextPermutation([1, 2, 3, 4]))
print(sol.nextPermutation([4, 3, 2, 1]))
print(sol.nextPermutation([1, 1, 5]))
print(sol.nextPermutation([1, 3, 2]))
print(sol.nextPermutation([1, 5, 1]))
