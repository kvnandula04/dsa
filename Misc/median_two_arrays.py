from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = sorted(nums1 + nums2)
        mid = len(merged_array) // 2
        # compute the average of the 1/2 middle numbers
        median = (merged_array[mid] + merged_array[~mid]) / 2

        return median


sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2]))  # Expected output: 2.0
