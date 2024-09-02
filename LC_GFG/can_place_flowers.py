class Solution:
    def canPlaceFlowers(self, flowerbed, n) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                next_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    n -= 1

        return n <= 0


sol = Solution()

# Example Test Cases
print("Test Case 1:", sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Expected output: True
print("Test Case 2:", sol.canPlaceFlowers([1, 0, 0, 0, 1], 2))  # Expected output: False

# Test Case 3: No space for any flowers
print("Test Case 3:", sol.canPlaceFlowers([1, 1, 1, 1, 1], 1))  # Expected output: False

# Test Case 4: All empty plots, should be able to plant n flowers
print("Test Case 4:", sol.canPlaceFlowers([0, 0, 0, 0, 0], 2))  # Expected output: True

# Test Case 5: More flowers than possible to plant
print("Test Case 5:", sol.canPlaceFlowers([0, 0, 0, 0], 3))  # Expected output: False

# Test Case 6: Alternating plots, already full
print("Test Case 6:", sol.canPlaceFlowers([1, 0, 1, 0, 1], 1))  # Expected output: False

# Test Case 7: Edge case with only one plot, can plant if empty
print("Test Case 7:", sol.canPlaceFlowers([0], 1))  # Expected output: True
print("Test Case 8:", sol.canPlaceFlowers([1], 1))  # Expected output: False

# Test Case 9: No flowers to plant, should always return true
print("Test Case 9:", sol.canPlaceFlowers([1, 0, 0, 0, 1], 0))  # Expected output: True

# Test Case 10: Full flowerbed but one gap where planting is possible
print("Test Case 10:", sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Expected output: True

# Test Case 11: Flowerbed with enough space to plant exactly n flowers
print(
    "Test Case 11:", sol.canPlaceFlowers([0, 0, 1, 0, 0, 1, 0, 0], 2)
)  # Expected output: True

# Test Case 12: Flowerbed with multiple small gaps
print(
    "Test Case 12:", sol.canPlaceFlowers([1, 0, 1, 0, 0, 0, 1], 1)
)  # Expected output: True

# Test Case 13: Large flowerbed with alternating empty and filled plots
print("Test Case 13:", sol.canPlaceFlowers([0, 1] * 500, 1))  # Expected output: False
