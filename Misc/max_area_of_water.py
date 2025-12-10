class Solution:
    def maxArea(self, height) -> int:
        start = 0
        end = len(height) - 1
        max_area = 0

        while start < end:
            area = (end - start) * min(height[start], height[end])

            if area > max_area:
                max_area = area
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return max_area


sol = Solution()
# Test case 1: Example provided in the problem statement
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Expected output: 49

# Test case 2: Smallest possible input
print(sol.maxArea([1, 1]))  # Expected output: 1

# Test case 3: All heights are the same
print(sol.maxArea([5, 5, 5, 5, 5]))  # Expected output: 20

# Test case 4: Increasing height array
print(sol.maxArea([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Expected output: 20

# Test case 5: Decreasing height array
print(sol.maxArea([9, 8, 7, 6, 5, 4, 3, 2, 1]))  # Expected output: 20

# Test case 6: Mixed heights
print(sol.maxArea([3, 1, 2, 4, 5, 3, 6]))  # Expected output: 15

# Test case 7: Single large height among small ones
print(sol.maxArea([1, 1, 1, 10, 1, 1, 1]))  # Expected output: 6

# Test case 8: Large input size with random values
print(
    sol.maxArea([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
)  # Expected output: 4500
