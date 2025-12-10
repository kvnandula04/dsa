class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        left = 0
        right = len(arr) - 1

        while left < right:  # Continue until left and right converge
            mid = left + (right - left) // 2

            if arr[mid] < arr[mid + 1]:  # Peak is to the right
                left = mid + 1
            else:  # Peak is to the left or at mid
                right = mid

        return left  # Can return left or right, since left == right at the peak


# Test case 1: Peak is in the middle of a small mountain array
arr1 = [0, 1, 0]
print(Solution().peakIndexInMountainArray(arr1))
# Expected output: 1 (peak at index 1)

# Test case 2: Peak is in the middle of a larger mountain array
arr2 = [0, 2, 1, 0]
print(Solution().peakIndexInMountainArray(arr2))
# Expected output: 1 (peak at index 1)

# Test case 3: Peak is in the middle of an even larger mountain array
arr3 = [0, 10, 5, 2]
print(Solution().peakIndexInMountainArray(arr3))
# Expected output: 1 (peak at index 1)

# Test case 4: Peak is at a different index in the array
arr4 = [3, 5, 3, 2, 0]
print(Solution().peakIndexInMountainArray(arr4))
# Expected output: 1 (peak at index 1)

# Test case 5: Larger array with peak further towards the end
arr5 = [0, 1, 2, 3, 4, 5, 3, 1]
print(Solution().peakIndexInMountainArray(arr5))
# Expected output: 5 (peak at index 5)

# Test case 6: Peak is near the start of the array
arr6 = [1, 3, 2, 1]
print(Solution().peakIndexInMountainArray(arr6))
# Expected output: 1 (peak at index 1)

# Test case 7: Array with the smallest allowed size where peak is clearly in the middle
arr7 = [1, 2, 1]
print(Solution().peakIndexInMountainArray(arr7))
# Expected output: 1 (peak at index 1)

# Test case 8: Larger mountain array with a gradual increase and sharp peak
arr8 = [0, 2, 4, 6, 8, 10, 7, 4, 2]
print(Solution().peakIndexInMountainArray(arr8))
# Expected output: 5 (peak at index 5)

# Test case 9: Large mountain array with peak in the middle (edge case for performance)
arr9 = list(range(1, 50001)) + list(range(49999, 0, -1))
print(Solution().peakIndexInMountainArray(arr9))
# Expected output: 49999 (peak at index 49999)

# Test case 10: Another large array but with a smaller peak
arr10 = [0] * 49999 + [1000000] + [0] * 49999
print(Solution().peakIndexInMountainArray(arr10))
# Expected output: 49999 (peak at index 49999)

# Test case 11:
print(Solution().peakIndexInMountainArray([40, 48, 61, 75, 100, 99, 98, 39, 30, 10]))
# Expected output: 4 (peak at index 4)
