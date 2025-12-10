class Solution:
    def firstMissingPositive(self, nums) -> int:
        real_nums = set(nums)  # Use a set to remove duplicates and improve lookup time

        for i in range(1, len(real_nums) + 2):  # Iterate from 1 to len(real_nums) + 1
            if i not in real_nums:
                return i

        return 1  # Return 1 if all positive integers are present


sol = Solution()

# Example Test Cases
print(sol.firstMissingPositive([3, 4, -1, 1]))  # Expected output: 2
print(sol.firstMissingPositive([7, 8, 9, 11, 12]))  # Expected output: 1
print(sol.firstMissingPositive([1, 2, 0]))  # Expected output: 3

# Additional Test Cases
print(sol.firstMissingPositive([1]))  # Expected output: 2  # Single Positive Element
print(sol.firstMissingPositive([-1]))  # Expected output: 1  # Single Negative Element
print(
    sol.firstMissingPositive([1, 2, 3, 4, 5])
)  # Expected output: 6  # Continuous Positive Integers
print(
    sol.firstMissingPositive([1, 1, 0, -1, -2])
)  # Expected output: 2  # Array with Duplicates
print(
    sol.firstMissingPositive([-10, -3, 1, 2, 3, 4, 5, 6, 7, 8])
)  # Expected output: 9  # Mix of Negatives and Positives
print(
    sol.firstMissingPositive([0, -1, -2])
)  # Expected output: 1  # Array with Zeroes and Negatives
print(sol.firstMissingPositive([]))  # Expected output: 1  # Empty Array
print(sol.firstMissingPositive([10, 20, 30, 40]))  # Expected output: 1  # Large Gaps
print(
    sol.firstMissingPositive([5, 6, 7, 9])
)  # Expected output: 1  # Non-Consecutive Positives
