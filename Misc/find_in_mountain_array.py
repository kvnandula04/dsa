# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """


# Method stubs here, Leetcode has the actual implementation
class MountainArray:
    def get(self, index: int) -> int:
        pass

    def length(self) -> int:
        pass


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        left = 0
        right = mountain_arr.length() - 1  # Corrected right boundary

        # Get peak
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak = left  # This is the peak index

        # Search before peak (ascending part)
        left = 0
        right = peak
        while left <= right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) < target:
                left = mid + 1
            else:
                right = mid - 1

        # Search after peak (descending part)
        left = peak
        right = mountain_arr.length() - 1  # Corrected right boundary
        while left <= right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) == target:
                return mid
            elif (
                mountain_arr.get(mid) > target
            ):  # Reverse condition for descending part
                left = mid + 1
            else:
                right = mid - 1

        return -1
